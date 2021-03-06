from app import app, admin, db, models
from flask import Flask
from flask.ext.admin import BaseView, expose
from flask import g
from flask.ext.admin.contrib.sqla import ModelView, fields
from flask.ext.admin.contrib.fileadmin import FileAdmin
import os.path as op
from config import SUPERUSERS
from wtforms import validators

path = op.join(op.dirname(__file__), 'static')


class MyBase(ModelView):
    def is_accessible(self):
        return g.user.is_authenticated() and (g.user.net_id in SUPERUSERS)

class MyFileAdmin(FileAdmin):
    def is_accessible(self):
        return g.user.is_authenticated() and (g.user.net_id in SUPERUSERS)

    
class QuerySelectMultipleFieldSet(fields.QuerySelectMultipleField):
    def populate_obj(self, obj, name):
        setattr(obj, name, set(self.data))

class ProfessorAdmin(MyBase):
    form_overrides = {
        'courses': QuerySelectMultipleFieldSet
    }

    form_args = {
      'courses': {
          'query_factory': lambda: db.session.query(models.Course)
      }
    }


   


class UserAdmin(MyBase):
    can_create = True

class CategoryAdmin(MyBase):
    pass

class ReviewAdmin(MyBase):
    can_create = True

class CourseAdmin(MyBase):
    form_args = dict(
                    professor=dict(label='Professor', validators=[validators.required()])
                )


class StaticFilesAdmin(MyFileAdmin):
    pass

admin.add_view(ProfessorAdmin(models.Professor, db.session))
admin.add_view(CourseAdmin(models.Course, db.session))
admin.add_view(CategoryAdmin(models.Category, db.session))
admin.add_view(UserAdmin(models.User, db.session))
admin.add_view(ReviewAdmin(models.Review, db.session))
admin.add_view(StaticFilesAdmin(path, '/static/', name='Static Files'))
