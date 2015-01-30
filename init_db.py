from main import create_app
from database import db
from api.models.todo import Todo
from api.models.course import Course
from api.models.course_version import CourseVersion
from api.models.instructor import Instructor

app = create_app()
app.config.from_object('config.Config')

with app.test_request_context():
  db.create_all()
