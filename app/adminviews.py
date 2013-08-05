from app import app, admin, db, models
from flask import Flask
from flask.ext.admin import BaseView, expose
from flask import g
from flask.ext.admin.contrib.sqlamodel import ModelView
from flask.ext.admin.contrib.fileadmin import FileAdmin
import os.path as op
from config import SUPERUSERS

path = op.join(op.dirname(__file__), 'static')

##class MyBase(ModelView):
##    def is_accessible(self):
##        return g.user.is_authenticated() #and (g.user.net_id in SUPERUSERS)
##
##class MyFileAdmin(FileAdmin):
##    def is_accessible(self):
##        return g.user.is_authenticated() #and g.user.net_id in SUPERUSERS
##
##    
##class QuerySelectMultipleFieldSet(fields.QuerySelectMultipleField):
##    def populate_obj(self, obj, name):
##        setattr(obj, name, set(self.data))
##
##class ProfessorAdmin(MyBase):
##    form_overrides = {
##        'courses': QuerySelectMultipleFieldSet
##    }
##
##class UserAdmin(MyBase):
##    can_create = False
##
##class CategoryAdmin(MyBase):
##    pass
##
##class ReviewAdmin(MyBase):
##    can_create = False
##
##class CourseAdmin(MyBase):
##    pass
##
##class StaticFilesAdmin(MyFileAdmin):
##    pass

admin.add_view(ModelView(models.Professor, db.session))
admin.add_view(ModelView(models.Course, db.session))
admin.add_view(ModelView(models.Category, db.session))
admin.add_view(ModelView(models.User, db.session))
admin.add_view(ModelView(models.Review, db.session))
admin.add_view(ModelView(path, '/static/', name='Static Files'))
