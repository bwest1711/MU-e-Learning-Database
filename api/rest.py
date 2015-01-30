from flask.ext import restful
from flask import Blueprint

from api.views.todo import TodoAPI
from api.views.todo import TodoListAPI

from api.views.course import CourseAPI
from api.views.course import CoursesAPI

from api.views.instructor import InstructorAPI
from api.views.instructor import InstructorsAPI

api_app = Blueprint('api_app', __name__, url_prefix='/api')
api = restful.Api(api_app)

api.add_resource(TodoListAPI, '/todos')
api.add_resource(TodoAPI, '/todos/<int:id>')

api.add_resource(InstructorAPI, '/instructors/<int:id>')
api.add_resource(InstructorsAPI, '/instructors')

api.add_resource(CourseAPI, '/courses/<int:id>')
api.add_resource(CoursesAPI, '/courses')
