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

    items = [
        # (Full Name, Email)
        Instructor("Eddard Stark", "starke4@wu.edu"),       # 1
        Instructor("Ramsay Snow", "snowr72@dfcc.org"),      # 2
        Instructor("Cersei Lannister", "lannisc2@ucr.edu"), # 3
        Instructor("Petyr Baelish", "baelisp@vale.edu"),    # 4
        Instructor("Jon Snow", "snowj41@wu.edu"),           # 5

        # (Title, Department, Number)
        Course("Intro to Criminal Justice", "CJS", "111"),     # 1
        Course("Human Anatomy", "BIO", "202"),                 # 2
        Course("Politics and National Issues", "POL", "182"),  # 3
        Course("Intro to Financial Accounting", "ACC", "221"), # 4
        Course("Principles of Acting", "THE", "131"),          # 5

        # (Course, Instructor, Label, Type, Copy Cmp., ADA Cmp., ADA Year)
        CourseVersion(1, 1, "Ned's version", "Hybrid", True, False),               # 1
        CourseVersion(1, 1, "New version Fall '13", "Online Only", False, True),        # 2
        CourseVersion(2, 2, "Emphasis on muscular system", "Hybrid", False, False), # 3
        CourseVersion(3, 3, "", "Online Only", True, False),                            # 4
        CourseVersion(3, 4, "Honors section", "Hybrid", True, True),              # 5
        CourseVersion(4, 4, "", "Online Only", True, True),                            # 6
        CourseVersion(5, 4, "", "Online Only", True, True),                            # 7

        # (Course Version, Instructor, Semester)
        CourseSection(2, 1, "F13"), # 1
        CourseSection(3, 2, "F13"), # 2
        CourseSection(7, 4, "S14"), # 3

        # (Course Version, Stage)
        QualityReview(2, "Author Review"),   # 1
        QualityReview(3, "Author Revision"), # 2
        QualityReview(3, "Author Review"),   # 3
        QualityReview(5, "ID Sign-off"),     # 4
        QualityReview(6, "Discussion"),      # 5
    ]

    for item in items:
        db.session.add(item)

    db.session.commit()
