# This file maps API resources (that implement GET, POST, etc.) to public-
# facing URLs that the client accesses

from flask.ext import restful
from flask import Blueprint

from api.views.todo import TodoAPI
from api.views.todo import TodoListAPI
from api.views.course import CourseAPI
from api.views.course import CoursesAPI
from api.views.instructor import InstructorAPI
from api.views.instructor import InstructorsAPI
from api.views.course_version import CourseVersionAPI
from api.views.course_version import CourseVersionsAPI
from api.views.course_section import CourseSectionAPI
from api.views.course_section import CourseSectionsAPI
from api.views.quality_review import QualityReviewAPI
from api.views.quality_review import QualityReviewsAPI
from api.views.search import SearchAPI

api_app = Blueprint('api_app', __name__, url_prefix='/api')
api = restful.Api(api_app)

api.add_resource(TodoListAPI, '/todos')
api.add_resource(TodoAPI, '/todos/<int:id>')

api.add_resource(InstructorAPI, '/instructors/<int:id>')
api.add_resource(InstructorsAPI, '/instructors')

api.add_resource(CourseAPI, '/courses/<int:id>')
api.add_resource(CoursesAPI, '/courses')

api.add_resource(CourseVersionAPI, '/course_versions/<int:id>')
api.add_resource(CourseVersionsAPI, '/course_versions')

api.add_resource(CourseSectionAPI, '/course_sections/<int:id>')
api.add_resource(CourseSectionsAPI, '/course_sections')

api.add_resource(QualityReviewAPI, '/quality_reviews/<int:id>')
api.add_resource(QualityReviewsAPI, '/quality_reviews')

api.add_resource(SearchAPI, '/search')
