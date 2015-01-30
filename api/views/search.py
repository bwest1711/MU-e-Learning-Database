from flask.ext import restful
from flask.ext.restful import reqparse
from database import db
from api.models.course import Course
from api.models.instructor import Instructor


class SearchAPI(restful.Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('term', type=str)
        parser.add_argument('crn', type=int)
        args = parser.parse_args()

        # Get list of matching courses
        courses = Course.query.order_by(Course.id.desc()).all()
        courses = [course.to_json for course in courses]

        return {'test': 'you searched for {}'.format(args['term'])}
