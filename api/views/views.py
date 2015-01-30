from flask.ext import restful
from flask.ext.restful import reqparse
from flask import Blueprint
from api.models.todo import Todo
from api.models.instructor import Instructor
from api.models.course import Course
from database import db

api_app = Blueprint('api_app', __name__, url_prefix='/api')
api = restful.Api(api_app)

class TodoListAPI(restful.Resource):
    def get(self):
        '''Get list of all todos'''
        todos = Todo.query.order_by(Todo.last_update.desc()).all()
        todos = [todo.as_json() for todo in todos]
        return {'todos': todos}

    def post(self):
        '''Create a new todo'''
        parser = reqparse.RequestParser()
        parser.add_argument('todo', type=dict, required=True)
        args = parser.parse_args()

        if args['todo']['description']:
            todo = Todo(args['todo']['description'])
            db.session.add(todo)
            db.session.commit()
            return {'todo': todo.as_json()}
        restful.abort(400, message='Missing description')


class TodoAPI(restful.Resource):
    def get(self, id):
        '''Get a specific todo'''
        todo = Todo.query.get(id)

        if not todo:
            restful.abort(404, message='Invalid todo')

        return {'todo': todo.as_json()}

    def put(self, id):
        '''Update a specific todo'''
        todo = Todo.query.get(id)

        if not todo:
            restful.abort(404, message='Invalid todo')

        parser = reqparse.RequestParser()
        parser.add_argument('todo', type=dict, required=True)
        args = parser.parse_args()

        try:
            todo.description = args['todo']['description']
            todo.is_completed = args['todo']['isCompleted']
        except:
            restful.session.abort(400)

        db.session.add(todo)
        db.session.commit()
        return {'todo': todo.as_json()}

    def delete(self, id):
        '''Delete a todo'''
        todo = Todo.query.get(id)
        if not todo:
            restful.abort(404, message='Invalid todo')

        db.session.delete(todo)
        db.session.commit()

api.add_resource(TodoAPI, '/todos/<int:id>')
api.add_resource(TodoListAPI, '/todos')

################################################################################

### INSTRUCTORS

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

api.add_resource(InstructorsAPI, '/instructors')
api.add_resource(InstructorAPI, '/instructors/<int:id>')


### COURSES

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

api.add_resource(CoursesAPI, '/courses')
api.add_resource(CourseAPI, '/courses/<int:id>')
