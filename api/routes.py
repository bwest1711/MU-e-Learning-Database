import flask
from flask.ext import restful
from flask.ext import restless
from api.models.instructor import Instructor
from api.models.course import Course
from api.models.course_version import CourseVersion
from api.models.course_section import CourseSection
from api.models.quality_review import QualityReview
from api.models.department import Department
from api.models.note import Note

################################################################################
# This file maps API resources (that implement GET, POST, etc.) to public-
# facing URLs that the client accesses. This essentially 'glues' the whole API
# together, and so it must be updated whenever a new model object is added.
################################################################################


# Function to actually create the API, including all CRUD wrappers, search 
# pages, and static pages
def create_api(app, db):

    # Methods we want to add to each model
    all_methods = ['GET', 'POST', 'PUT', 'DELETE']

    # [Name of class, serialized pluralized name]
    models = [
        [Instructor, 'instructors'],
        [Department, 'departments'],
        [Course, 'courses'],
        [CourseVersion, 'courseVersions'],
        [CourseSection, 'courseSections'],
        [QualityReview, 'qualityReviews'],
        [Note, 'notes']
    ]
    manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

    # Create an API for each model object
    for model, model_name in models:
        postprocessors = get_postprocessors(model_name)
        preprocessors = get_preprocessors(model_name)
        manager.create_api(model, 
                           collection_name=model_name,
                           preprocessors=preprocessors,
                           postprocessors=postprocessors,
                           methods=all_methods)


# Below are some custom helpers to format Flask's responses into Ember's format.

# Flask-Restless returns JSON inside a generic top-level "objects" object, 
# whereas Ember wants the top-level object to have the name of the class, 
# like { 'instructors': [ {...}, {...} ] }. We can define pre- and post-
# processors for Flask-Restless's responses to transform them in this way. 

# Credit to Drew Larson @ drwlrsn.com

def get_preprocessors(model_name):
    '''Gets pre-processing methods for flask-restless to use, customized on a 
    per-class basis to return the JSON format that Ember expects'''

    def pre_ember_formatter(data, **kw):
        top_level = data.keys()[0]
        for key in data[top_level]:
            data[key] = data[top_level][key]
        del data[top_level]

    # 'data' comes in as e.g. {'instructor':{'fullName':...}}. Flask-Restless
    # wants it as a group of simple key/value pairs. 
    def pre_patch_ember_formatter(instance_id, data):
        top_level = data.keys()[0]
        for k, v in data[top_level].items():
            data[k] = v
        del data[top_level]

    return {
        'POST': [pre_ember_formatter],
        'PUT_SINGLE': [pre_patch_ember_formatter]
    }

def get_postprocessors(model_name):
    '''Gets post-processing methods for flask-restless to use, customized on a 
    per-class basis to return the JSON format that Ember expects'''

    def post_collection_formatter(result, search_params):
        for key in result.keys():
            if key != 'objects':
                del result[key]
        result[model_name] = result['objects']
        del result['objects']

    # Need to find a better solution for this...
    # Restless expects all dictionary operations to be done in-place on the 
    # 'result' object, but what we want to return is a new dict in the format 
    # { 'model_name': <result dict> }. Copy is the easy way to do it, but 
    # there must be a more efficient method
    def post_singular_formatter(result):
        result[model_name] = [result.copy()]
        for key in result.keys():
            if key != model_name:
                del result[key]

    return { 
        'GET_SINGLE': [post_singular_formatter],
        'GET_MANY': [post_collection_formatter],
        'POST': [post_singular_formatter],
        'PUT_SINGLE': [post_singular_formatter]
    }
