from main import create_app
from database import db
from api.models.instructor import Instructor
from api.models.course import Course
from api.models.course_version import CourseVersion

app = create_app()
app.config.from_object('config.Config')

with app.test_request_context():
    db.session.query(Instructor).delete()
    db.session.query(Course).delete()
    db.session.commit()

    db.session.add(Instructor('Eddard Stark', 'starke4@wu.edu'))
    db.session.add(Instructor('Ramsay Snow', 'snowr72@dfcc.org'))
    db.session.add(Instructor('Cersei Lannister', 'lannisc2@ucr.edu'))
    db.session.add(Instructor('Peter Baelish', 'baelisp@vale.edu'))

    db.session.add(Course('Intro to Criminal Justice', 'CJS', '111'))
    db.session.add(Course('Human Anatomy', 'BIO', '202'))
    db.session.add(Course('Politics and National Issues', 'POL', '182'))
    db.session.add(Course('Intro to Financial Accounting', 'ACC', '221'))
    db.session.add(Course('Principles of Acting', 'THE', '131'))

    db.session.commit()
