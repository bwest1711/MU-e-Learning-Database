from flask.ext import restful
from flask.ext.restful import reqparse
from database import db
from sqlalchemy import and_
from api.models.course import Course
from api.models.instructor import Instructor


class SearchAPI(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('crn', type=int)
        parser.add_argument('instructor', type=str)
        parser.add_argument('hasReview', type=bool)
        parser.add_argument('courseType', type=str)
        parser.add_argument('dueForReviewSoon', type=bool)
        parser.add_argument('hasADAForm', type=bool)
        parser.add_argument('copyrightCompliant', type=bool)
        args = parser.parse_args()

        # Add only the conditions that have been specified
        conditions = []
        if args['title'] is not None:
            conditions.append(Course.title.like("%{}%".format(args['title'])))


        # Get a list of all courses that meet criteria.
        # 'and_' is used to batch query all conditions simultaneously, rather 
        # than query the entire list and then filtering one by one
        courses = Course.query.filter(and_(*conditions)).all()
        courses = [course.to_json for course in courses]

        return { "results" : courses }
