from main import create_app
from database import db
from api.models.instructor import Instructor
from api.models.course import Course
from api.models.course_version import CourseVersion
from api.models.course_section import CourseSection
from api.models.quality_review import QualityReview

app = create_app()
app.config.from_object('config.Config')

with app.test_request_context():
    db.session.query(Instructor).delete()
    db.session.query(Course).delete()
    db.session.query(CourseVersion).delete()
    db.session.query(CourseSection).delete()
    db.session.query(QualityReview).delete()
    db.session.commit()

    db.session.add(Instructor("Eddard Stark", "starke4@wu.edu"))
    db.session.add(Instructor("Ramsay Snow", "snowr72@dfcc.org"))
    db.session.add(Instructor("Cersei Lannister", "lannisc2@ucr.edu"))
    db.session.add(Instructor("Peter Baelish", "baelisp@vale.edu"))
    db.session.add(Instructor("Jon Snow", "snowj41@wu.edu"))

    db.session.add(Course("Intro to Criminal Justice", "CJS", "111"))
    db.session.add(Course("Human Anatomy", "BIO", "202"))
    db.session.add(Course("Politics and National Issues", "POL", "182"))
    db.session.add(Course("Intro to Financial Accounting", "ACC", "221"))
    db.session.add(Course("Principles of Acting", "THE", "131"))

    db.session.add(CourseVersion(1, 1, "Ned's version"))
    db.session.add(CourseVersion(1, 1, "New version Fall '13"))
    db.session.add(CourseVersion(2, 2, "Emphasis on muscular system"))
    db.session.add(CourseVersion(3, 3, ""))
    db.session.add(CourseVersion(3, 4, "Honors section"))
    db.session.add(CourseVersion(4, 4, ""))
    db.session.add(CourseVersion(5, 4, ""))

    db.session.add(CourseSection(2, 1, "F13"))
    db.session.add(CourseSection(3, 2, "F13"))
    db.session.add(CourseSection(7, 4, "S14"))

    db.session.add(QualityReview(2, "Author Review"))
    db.session.add(QualityReview(3, "Author Revision"))
    db.session.add(QualityReview(3, "Author Review"))
    db.session.add(QualityReview(5, "ID Sign-off"))
    db.session.add(QualityReview(6, "Discussion"))

    db.session.commit()
