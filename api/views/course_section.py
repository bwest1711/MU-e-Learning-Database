from flask.ext import restful
from flask.ext.restful import reqparse
from database import db
from api.models.course_section import CourseSection


class CourseSectionsAPI(restful.Resource):
    def get(self):
        '''Get list of all course sections'''
        course_sections = CourseSection.query.order_by(CourseSection.id.asc()).all()
        course_sections = [course_section.to_json for course_section in course_sections]
        return {'course_sections': course_sections}

    # TODO
    def post(self):
        pass


class CourseSectionAPI(restful.Resource):
    def get(self, id):
        '''Get a specific course section'''
        course_section = CourseSection.query.get(id)

        if not course_section:
            restful.abort(404, message='Invalid course section')

        return {'course_section': course_section.to_json}

    # TODO
    def put(self, id):
        pass

    # TODO
    def delete(self, id):
        pass
