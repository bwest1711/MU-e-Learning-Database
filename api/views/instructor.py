from flask.ext import restful
from flask.ext.restful import reqparse
from database import db
from api.models.instructor import Instructor


class InstructorsAPI(restful.Resource):
    def get(self):
        '''Get list of all instructors'''
        instructors = Instructor.query.order_by(Instructor.id.desc()).all()
        instructors = [instructor.to_json for instructor in instructors]
        return {'instructors': instructors}

    def post(self):
        '''Create a new instructor'''
        parser = reqparse.RequestParser()
        parser.add_argument('instructor', type=dict, required=True)
        args = parser.parse_args()

        if args['instructor']['description']:
            instructor = Instructor(args['instructor']['description'])
            db.session.add(instructor)
            db.session.commit()
            return {'instructor': instructor.as_json()}
        restful.abort(400, message='Missing description')


class InstructorAPI(restful.Resource):
    def get(self, id):
        '''Get a specific instructor'''
        instructor = Instructor.query.get(id)

        if not instructor:
            restful.abort(404, message='Invalid instructor')

        return {'instructor': instructor.to_json}

    def put(self, id):
        '''Update a specific instructor'''
        instructor = Instructor.query.get(id)

        if not instructor:
            restful.abort(404, message='Invalid instructor')

        parser = reqparse.RequestParser()
        parser.add_argument('instructor', type=dict, required=True)
        args = parser.parse_args()

        try:
            instructor.full_name = args['instructor']['full_name']
            instructor.email = args['instructor']['email']
        except:
            restful.session.abort(400)

        db.session.add(instructor)
        db.session.commit()
        return {'instructor': instructor.to_json()}

    def delete(self, id):
        '''Delete a instructor'''
        instructor = Instructor.query.get(id)
        if not instructor:
            restful.abort(404, message='Invalid instructor')

        db.session.delete(instructor)
        db.session.commit()
