from main import create_app
from database import db
from api.models.course import Course
from api.models.course_version import CourseVersion
from api.models.course_section import CourseSection
from api.models.instructor import Instructor
from api.models.quality_review import QualityReview

app = create_app()
app.config.from_object('config.Config')

with app.test_request_context():
  db.create_all()
