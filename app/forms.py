from flask.ext.wtf import Form, SelectField, TextAreaField, HiddenField, TextField
from flask.ext.wtf import Required, Length

class reviewSubmissionForm(Form):
    rating = SelectField('rating', choices = [('', ''),('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators = [Required('Please select a rating out of 5 for the course quality.')])
    comment = TextAreaField('comment',validators = [Required('Please write a review.'), Length(min=100,message="Please write at least 100 characters.")])



class searchForm(Form):
    search = TextField('search',validators = [Required("Please enter keyword or the entire course name.")])

class courseSubmissionForm(Form):
    course = TextField('course',validators = [Required("Please enter a course name")])
    professor = TextField('professor',validators = [Required("Please enter a professor name")])
    
   
