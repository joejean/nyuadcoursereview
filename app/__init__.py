from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask_mail import Mail
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
from momentjs import momentjs
from flask.ext.admin import Admin
import os


app = Flask(__name__)
app.config.from_object('config')
admin = Admin(app, name ="NYUAD Course Review")
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
mail = Mail(app)
app.jinja_env.globals['momentjs'] = momentjs

#send an email when there is an 500 error
if not app.debug and os.environ.get('HEROKU') is None:
    import logging
    from logging.handlers import SMTPHandler, RotatingFileHandler
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler ((MAIL_SERVER, MAIL_PORT), 'no-reply@'+ MAIL_SERVER, ADMINS, 'Nyuad Course Review Failure', credentials)

    #save the errors in the temp file on our server 
    file_handler = RotatingFileHandler('tmp/coursereview.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('NYUAD Course Review')

if os.environ.get('HEROKU') is not None:
    import logging
    stream_handler = logging.StreamHandler()
    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('NYUAD Course Review')

from app import views, models

