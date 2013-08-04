#config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))


CSRF_ENABLED = True
SECRET_KEY = '\x00\x18}{\x9b\xa4(\xaa\xf7[4\xd5Ko\x07S\x03#%_cM\xf2y.\xf6\xf00Kr'

#NYU user Groups not allowed to login
RESTRICTED_GROUPS =["nyu-admins", "admins", "nyu-it"]
# Search
MAX_SEARCH_RESULTS = 15
WHOOSH_BASE = os.path.join(basedir, 'search.db')

#Database URI
if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:police12345@localhost:5432/nyuadcoursereview'
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

#SQLiteURI 'sqlite:///' + os.path.join(basedir, 'app.db')

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#Site ADMINS
SUPERUSERS=["jj1347"]

#Mail Server Settings
MAIL_SERVER ='http://www.outlook.com'
MAIL_PORT ='25'
MAIL_USERNAME ='joeclef@hotmail.com'
MAIL_DEFAULT_SENDER = 'joeclef@hotmail.com'
MAIL_PASSWORD ='2012@yitiapdekol!'
ADMINS = ['joeclef@hotmail.com', 'jj1347@nyu.edu']


#Pagination

POST_PER_PAGE_SHORT = 2
POST_PER_PAGE_LONG = 1

#Settings for Disabling Full text Search when running on Heroku
WHOOSH_ENABLED = os.environ.get('HEROKU') is None
