from flask.ext import restful
from flask.ext.restful import reqparse
from database import db
from api.models.course import Course


class CoursesAPI(restful.Resource):
    def get(self):
        '''Get list of all courses'''
        courses = Course.query.order_by(Course.id.desc()).all()
        courses = [course.to_json for course in courses]
        return {'courses': courses}

    def post(self):
        '''Create a new course'''
        parser = reqparse.RequestParser()
        parser.add_argument('course', type=dict, required=True)
        args = parser.parse_args()

        if args['course']['description']:
            course = Course(args['course']['description'])
            db.session.add(course)
            db.session.commit()
            return {'course': course.as_json()}
        restful.abort(400, message='Missing description')


class CourseAPI(restful.Resource):
    def get(self, id):
        '''Get a specific course'''
        course = Course.query.get(id)

        if not course:
            restful.abort(404, message='Invalid course')

        return {'course': course.to_json}

    def put(self, id):
        '''Update a specific course'''
        course = Course.query.get(id)

        if not course:
            restful.abort(404, message='Invalid course')

        parser = reqparse.RequestParser()
        parser.add_argument('course', type=dict, required=True)
        args = parser.parse_args()

        try:
            course.title = args['course']['title']
            course.department = args['course']['department']
            course.number = args['course']['number']
        except:
            restful.session.abort(400)

        db.session.add(course)
        db.session.commit()
        return {'course': course.to_json()}

    def delete(self, id):
        '''Delete a course'''
        course = Course.query.get(id)
        if not course:
            restful.abort(404, message='Invalid course')

        db.session.delete(course)
        db.session.commit()
