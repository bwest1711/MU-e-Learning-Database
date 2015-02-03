# This file maps API resources (that implement GET, POST, etc.) to public-
# facing URLs that the client accesses

from flask.ext import restful
from flask import Blueprint

# Most of these are simple CRUD wrappers around the ORM model
from api.views.wrapper import make_wrapper_api
from api.models.instructor import Instructor
from api.models.course import Course
from api.models.course_version import CourseVersion
from api.models.course_section import CourseSection
from api.models.quality_review import QualityReview

# Everything else is a custom 'view'
from api.views.search import SearchAPI

# Original todo-list project code, kept around for sanity-checking reasons
from api.views.todo import TodoAPI
from api.views.todo import TodoListAPI

# The API app itself
api_app = Blueprint('api_app', __name__, url_prefix='/api')
api = restful.Api(api_app)

# (If this part breaks, something has gone very wrong)
api.add_resource(TodoListAPI, '/todos')
api.add_resource(TodoAPI, '/todos/<int:id>')

# Custom views

api.add_resource(SearchAPI, '/search')

# Basic CRUD wrappers

InstructorAPI, InstructorsAPI = make_wrapper_api(
    model_class=Instructor, 
    singular_name='instructor', 
    plural_name='instructors', 
    reqd_args={ 'full_name': str }, 
    opt_args={ 'email': str })
api.add_resource(InstructorAPI, '/instructors/<int:id>')
api.add_resource(InstructorsAPI, '/instructors')

CourseAPI, CoursesAPI = make_wrapper_api(
    model_class=Course, 
    singular_name='course', 
    plural_name='courses', 
    reqd_args={ 'title': str, 'department': str, 'number': int }, 
    opt_args={})
api.add_resource(CourseAPI, '/courses/<int:id>')
api.add_resource(CoursesAPI, '/courses')

CourseVersionAPI, CourseVersionsAPI = make_wrapper_api(
    model_class=CourseVersion, 
    singular_name='courseVersion', 
    plural_name='courseVersion', 
    reqd_args={ 'course_id': int, 'instructor_id': int, 'label': str }, 
    opt_args={})
api.add_resource(CourseVersionAPI, '/courseVersions/<int:id>')
api.add_resource(CourseVersionsAPI, '/courseVersions')

CourseSectionAPI, CourseSectionsAPI = make_wrapper_api(
    model_class=CourseSection, 
    singular_name='courseSection', 
    plural_name='courseSection', 
    reqd_args={
        'course_version_id': int, 'instructor_id': int, 'semester': str }, 
    opt_args={})
api.add_resource(CourseSectionAPI, '/courseSections/<int:id>')
api.add_resource(CourseSectionsAPI, '/courseSections')

QualityReviewAPI, QualityReviewsAPI = make_wrapper_api(
    model_class=QualityReview, 
    singular_name='qualityReview', 
    plural_name='qualityReviews', 
    reqd_args={'course_version_id': int, 'stage': str}, 
    opt_args={})
api.add_resource(QualityReviewAPI, '/qualityReviews/<int:id>')
api.add_resource(QualityReviewsAPI, '/qualityReviews')
