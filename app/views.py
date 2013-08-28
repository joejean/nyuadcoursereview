from flask import Flask, render_template, request, make_response, redirect, url_for, g, flash, session, abort
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic
from flask.ext.login import login_user, logout_user, login_required, current_user
from app import app, lm, db, models, mail, cache
from flask_mail import Message
from forms import reviewSubmissionForm, searchForm, courseSubmissionForm
from app import oauthLogin
from models import User, Review, Category, Course, Like, Professor
from config import POST_PER_PAGE_SHORT, POST_PER_PAGE_LONG , SUPERUSERS, MAIL_DEFAULT_SENDER, MAX_SEARCH_RESULTS, AUTHORIZED_GROUPS, ADMINS
from sqlalchemy.sql import func
from sqlalchemy_searchable import search
import json


# Instantiate Authomatic.
authomatic = Authomatic(oauthLogin.oauthconfig, '\x00\x18}{\x9b\xa4(\xaa\xf7[4\xd5Ko\x07S\x03#%_cM\xf2y.\xf6\xf00Kr', report_errors=False)

lm.login_view = "landing"
lm.login_message = "You must be logged in to view the requested page."
lm.login_message_category = "error"

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user
    g.search_form = searchForm()
    g.courses=[]
    courses = Course.query.all()
    for c in courses:
        g.courses.append(c.course_name)
    
    


#LANDING and  HOMEPAGE , ABOUT and TERMS of USE VIEWS


@app.route('/landing')
def landing():
    if g.user.is_authenticated():
        return redirect(url_for('home'))
    next_url = request.args.get('next')
    cache.set('next_url', next_url, 60)
    return render_template('landing.html', title ="Welcome")


@app.route('/about')
def about():
    return render_template('about.html', title ="About")


@app.route('/termsofuse')
def termsofuse():
    return render_template('termsofuse.html', title ="Terms of Use")

@app.route('/')
@app.route('/home')
@login_required
def home():
    categories = Category.query.order_by(Category.category_name)
    latest_reviews = Review.query.order_by(Review.review_date.desc()).all()[0:2]
    
    #Most reviewwed courses , starting with those that have at least 2 reviews.
    most_reviewed_course_id_subquery = db.session.query(Review.course_id, func.count(Review.course_id).label("count")).\
                                    group_by(Review.course_id).having(func.count(Review.course_id) > 1).subquery()

    most_reviewed_courses = db.session.query( Course, most_reviewed_course_id_subquery.c.count).join(most_reviewed_course_id_subquery).\
              order_by(most_reviewed_course_id_subquery.c.count.desc()).all()[0:30]

    #Top rated courses
    #func.avg(Review.rating) >= 3
    top_rated_course_id_subquery = db.session.query(Review.course_id, func.avg(Review.rating).label("rating"), func.count(Review.course_id).label("count")).\
                                    group_by(Review.course_id).having(func.count(Review.course_id) > 2).subquery()

    top_rated_courses = db.session.query( Course, top_rated_course_id_subquery.c.rating, top_rated_course_id_subquery.c.count).join(top_rated_course_id_subquery).\
              order_by(top_rated_course_id_subquery.c.rating.desc()).all()
    
    

    return render_template('home.html', categories = categories, courses=most_reviewed_courses, trcourses= top_rated_courses, reviews= latest_reviews, title="Home" )


#SEARCH VIEWS

@app.route('/search', methods = ['POST'])
@login_required
def search():
    if not g.search_form.validate_on_submit():
        return redirect(url_for('home'))
    return redirect(url_for('search_results', query = g.search_form.search.data))

@app.route('/search_results/<query>')
@login_required
def search_results(query):
    #Article.query.search(u'Finland').limit(5).all()
    results = Course.query.search(unicode(query)).limit(MAX_SEARCH_RESULTS).all()
    return render_template('searchresults.html',query = query, results = results, title ="Search Results")



# COURSES BY MAJOR VIEW

@app.route('/courses-by-major/<int:catid>/')
@app.route('/courses-by-major/<int:catid>/<int:page>')
@login_required
def coursesbymajor(catid, page=1):
    if catid < 1:
        abort(404)
    category = Category.query.get_or_404(catid)
    categories = Category.query.order_by(Category.category_name)

    courses = Course.query.filter(Course.categories.any(category_name=category.category_name)).order_by(Course.course_name).paginate(page, POST_PER_PAGE_LONG,False)
    
    
    return render_template('courses-by-major.html', category = category, categories = categories, courses = courses, title="Courses By Major" )

#COURSE SUBMISSION VIEW
@app.route('/submitcourse', methods=['GET', 'POST'])
@login_required
def submitcourse():
    form = courseSubmissionForm()
    if form.validate_on_submit():
        
        msg = Message("Course Submission", sender = MAIL_DEFAULT_SENDER, recipients = ADMINS)
        msg.body = """
        From: <%s>
        Course: %s
        Professor: %s
        """ % (g.user.net_id, form.course.data, form.professor.data)
        mail.send(msg)
        flash("Course submitted. Admins will add it as soon as possible.","success")
        return redirect('home')
    
    return render_template('submitcourse.html',form = form, title= "Submit Course")


#REVIEWS VIEWS

@app.route('/write/<int:courseid>', methods=['GET', 'POST'])
@login_required
def write(courseid):
    if courseid < 0:
        abort(404)
    course = Course.query.get_or_404(courseid)
    
    from datetime import datetime
    
    form = reviewSubmissionForm()
    if form.validate_on_submit():
        try:
            
            review = models.Review(review_date= datetime.utcnow(), review_comment=form.comment.data, rating =int(form.rating.data), course_id=course.id,\
                                   user_id =g.user.id)
            db.session.add(review)
            db.session.commit()
            flash("Review posted successfully","success")
            return redirect('home')
        except:
            db.session.rollback()
            flash("Sorry you can't post more than one review for a single course. Please edit the former one below.", "error")
            return redirect(url_for('editreview',courseid = course.id, userid = g.user.id))
    return render_template('write.html',form = form, course=course, edit = False, title = "Write Review")


@app.route('/editreview/<int:courseid>/<int:userid>', methods=['GET', 'POST'])
@login_required
def editreview(courseid, userid):
    if courseid < 0:
        abort(404)
    user = User.query.get_or_404(userid)
    course = Course.query.get_or_404(courseid)
    
    from datetime import datetime
    review = Review.query.filter_by(course_id=courseid, user_id=userid).first()
    if review.user_id != g.user.id and g.user.net_id not in SUPERUSERS:
            flash('You cannot edit someonelse review.',"error")
            return redirect(url_for('home'))
    form = reviewSubmissionForm()
    if form.validate_on_submit():
        review.rating = int(form.rating.data)
        review.review_comment = form.comment.data
        review.review_date = datetime.utcnow()
        db.session.commit()
        flash("Review edited successfully","success")
        return redirect('home')
    
    return render_template('write.html',form = form, course=course, rating=review.rating, \
                           comment=review.review_comment, edit =True, title = "Edit Review")

@app.route('/reviews/<int:courseid>')
@app.route('/reviews/<int:courseid>/<int:page>')
@login_required
def reviews(courseid, page = 1):
    if courseid < 1:
        abort(404)
    course= Course.query.get_or_404(courseid)
    reviews = Review.query.filter_by(course_id=course.id).order_by(Review.review_date.desc()).paginate(page, POST_PER_PAGE_SHORT, False)
    avgrating = (db.session.query(func.avg(models.Review.rating)).filter_by(course_id = course.id)[0])[0]
    if avgrating ==None:
        avgrating=0
    avgrating = "{0:.2f}".format(avgrating)
    totalreviews= reviews.total
    return render_template('course-reviews-list.html', user = g.user, reviews= reviews, course =course, totalreviews=totalreviews,\
                           avgrating =avgrating, title=course.course_name)

@app.route('/deletereview/<int:reviewid>')
@login_required
def deletereview(reviewid):
    review = Review.query.get(reviewid)
    if review == None:
        flash('Review not found.',"error")
        return redirect(url_for('home'))
    if review.user_id != g.user.id and g.user.net_id not in SUPERUSERS:
        flash('You cannot delete this review.',"error")
        return redirect(url_for('home'))
    db.session.delete(review)
    db.session.commit()
    flash('Your review has been deleted.',"success")
    return redirect(url_for('user', netID=g.user.net_id))


#USER RELATED VIEWS

@app.route('/user/<netID>/')
@app.route('/user/<netID>/<int:page>')
@login_required
def user(netID, page = 1):
    
    netID = netID.lower()
    user = User.query.filter_by(net_id = netID).first()
    if user == None:
        abort(404)
    elif user!=g.user and g.user.net_id not in SUPERUSERS:
        flash("Sorry, You can't see someone else's profile", "error")
        return redirect('home')

    reviews = Review.query.filter_by(user_id=user.id).order_by(Review.review_date.desc()).paginate(page, POST_PER_PAGE_SHORT, False)
    
    return render_template('userprofile.html',user = user,reviews = reviews, title="User Profile")


#ERRORS VIEWS

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Not Found"), 404

@app.errorhandler(500)
def server_error(e):
    db.session.rollback()
    return render_template('500.html', title="Server Error"),500



#LOGIN AND LOGOUT VIEWS

@app.route('/login', methods=['GET', 'POST'])     
@app.route('/login/<provider_name>/', methods=['GET', 'POST'])    
def login(provider_name='nyuad'):
    """
    Login handler, must accept both GET and POST to be able to use OpenID.
    """
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('home'))
    
    # We need response object for the WerkzeugAdapter.
    response = make_response()
    
    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name)
   
    
    # If there is no LoginResult object, the login procedure is still pending.
    if result:
        if result.user:
            # We need to update the user to get more info.
            result.user.update()
            #Check if passport returns an error, if so, that means the user is not a student, therefore we redirect the user to landing
            if hasattr(result.user, "error"):
                flash("Sorry, it seems that you are not a student, so you can't use NYUAD Coursereview.", "error")
                return redirect(url_for('landing'))
            #Check the user group, if belongs to any restricted group redirect login
##            for gr in result.user.groups:
##                if gr in AUTHORIZED_GROUPS:
##                    authorized = True
##                    break
##                else:
##                    authorized = False
##                    
##            if not authorized:
##                flash("Sorry, it seems that you are not a student, so you can't use NYUAD Coursereview.", "error")
##                return redirect(url_for('landing'))
            
            #check if the user is in the database already
            user = User.query.filter_by(net_id = result.user.NetID).first()
            if user is None:
                user = User(net_id = result.user.NetID)
                db.session.add(user)
                db.session.commit()
            
            login_user(user, remember=True)
            flash("You were logged in successfully.", "success")
        # The rest happens inside the template.
        return redirect(cache.get('next_url') or url_for('home'))
    
    # Don't forget to return the response.
    return response

@app.route ('/logout')
def logout():
    logout_user() #logout with flask-login
    return redirect('http://passport.sg.nyuad.org/auth/logout')#logout with passport

