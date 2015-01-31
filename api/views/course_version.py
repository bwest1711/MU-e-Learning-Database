from flask.ext import restful
from flask.ext.restful import reqparse
from database import db
from api.models.course_version import CourseVersion


class CourseVersionsAPI(restful.Resource):
    def get(self):
        '''Get list of all course versions'''
        course_versions = CourseVersion.query.order_by(CourseVersion.id.desc()).all()
        course_versions = [course_version.to_json for course_version in course_versions]
        return {'course_versions': course_versions}

    def post(self):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        # TODO
        course_version = CourseVersion(args['course_version']['description'])
        db.session.add(course_version)
        db.session.commit()
        return {'course_version': course_version.as_json()}


class CourseVersionAPI(restful.Resource):
    def get(self, id):
        '''Get a specific course version'''
        course_version = CourseVersion.query.get(id)

        if not course_version:
            restful.abort(404, message='Invalid course version')

        return {'course_version': course_version.to_json}

    # TODO
    def put(self, id):
        '''Update a specific course version'''
        course_version = CourseVersion.query.get(id)

        if not course_version:
            restful.abort(404, message='Invalid course_version')

        parser = reqparse.RequestParser()
        parser.add_argument('course_version', type=dict, required=True)
        args = parser.parse_args()

        try:
            course_version.title = args['course_version']['title']
            course_version.department = args['course_version']['department']
            course_version.number = args['course_version']['number']
        except:
            restful.session.abort(400)

        db.session.add(course_version)
        db.session.commit()
        return {'course_version': course_version.to_json()}

    def delete(self, id):
        '''Delete a course version'''
        course_version = CourseVersion.query.get(id)
        if not course_version:
            restful.abort(404, message='Invalid course_version')

        db.session.delete(course_version)
        db.session.commit()
