from datetime import date
from main import create_app
from database import db
from api.models.instructor import Instructor
from api.models.course import Course
from api.models.course_version import CourseVersion
from api.models.course_section import CourseSection
from api.models.quality_review import QualityReview
from api.models.department import Department
from api.models.note import Note

app = create_app()
app.config.from_object('config.Config')

with app.test_request_context():

    # First delete EVERYTHING in the database so we can work with a blank slate.

    # Note that this is hilariously dangerous and shouldn't really touch any
    # production server. TODO Add a double-triple-check 'Are you sure??' dialog
    db.session.query(Instructor).delete()
    db.session.query(Course).delete()
    db.session.query(CourseVersion).delete()
    db.session.query(CourseSection).delete()
    db.session.query(QualityReview).delete()
    db.session.query(Department).delete()
    db.session.query(Note).delete()
    db.session.commit()

    items = [

        # (Full Name, Email, UniqueID)
        Instructor("Jamie Langford" , "langfojc@miamioh.edu"  , "langfojc"  ) , # 1
        Instructor("Marc Rothwell"  , "rothwemm@miamioh.edu"  , "rothwemm"  ) , # 2
        Instructor("Raymond Gordon" , "gordonrt2@miamioh.edu" , "gordonrt2" ) , # 3
        Instructor("Jean Collins"   , "collinjg@miamioh.edu"  , "collinjg"  ) , # 4
        Instructor("Kristen Hall"   , "hallka10@miamioh.edu"  , "hallka10"  ) , # 5

        # (Title, Department, Number)
        Course("Intro to Criminal Justice"     , 2 , "111") , # 1
        Course("Human Anatomy"                 , 1 , "202") , # 2
        Course("Politics and National Issues"  , 3 , "182") , # 3
        Course("Intro to Financial Accounting" , 4 , "221") , # 4
        Course("Principles of Acting"          , 5 , "131") , # 5

        # (Course, Instructor, Label, Type, Copy Cmp., ADA Cmp., ADA Year)
        CourseVersion(1, 1, "Hybrid version", "Hybrid", True, False),               # 1
        CourseVersion(1, 1, "New version Fall '13", "Online Only", False, True),    # 2
        CourseVersion(2, 2, "202 Master Version", "Hybrid", False, False), # 3
        CourseVersion(3, 3, "Sprint version", "Online Only", True, False),          # 4
        CourseVersion(3, 4, "Honors section", "Hybrid", True, True),                # 5
        CourseVersion(4, 4, "", "Online Only", True, True),                         # 6
        CourseVersion(5, 4, "", "Online Only", True, True),                         # 7

        # (Course Version, Instructor, Semester, CRN)
        CourseSection(2, 1, "F13", "18273", 
                      attested=True, attestedDueDate=date(2013, 6, 25), 
                      attestedDate=date(2013, 6, 20), 
                      attestedSignee="Jamie Langford"), # 1
        CourseSection(3, 2, "F13", "44953", attestedDueDate=date(2014, 7, 1)), # 2
        CourseSection(7, 4, "S14", "76182", attestedDueDate=date(2014, 1, 30)), # 3
        CourseSection(4, 4, "F14", "20315", attestedDueDate=date(2014, 6, 28)), # 4

        # (Course Version, Stage, Start Date, End Date)
        QualityReview(2, 0, date(2015, 1, 13), date(2015,  2, 20)), # 1
        QualityReview(3, 2, date(2012, 7,  3), date(2012,  7,  5)), # 3
        QualityReview(3, 1, date(2013, 6,  9), date(2013,  9, 29)), # 2
        QualityReview(5, 3, date(2014, 4, 20), date(2014,  5, 12)), # 4
        QualityReview(6, 4, date(2011, 9, 25), date(2011, 10, 14)), # 5

        # (Name, Abbreviation, Administrator, Admin Email, Aliases)
        Department("Biology", "BIO", "Daniel Whittington", "whittidj@miamioh.edu", ""),          # 1
        Department("Criminal Justice", "CJS", "Veronica Stephens", "stepheva7@miamioh.edu", ""), # 2
        Department("Political Science", "POL", "Brian Cameron", "camerobm@miamioh.edu", ""),     # 3
        Department("Accounting", "ACC", "Christine Rouillard", "rouillcd@miamioh.edu", ""),      # 4
        Department("Theatre", "THE", "Timothy Fisher", "fishertb3@miamioh.edu", ""),             # 5
        Department("History", "HST", "Amber Calvert", "calverag2@miamioh.edu", "")               # 6
    ]

    for item in items:
        db.session.add(item)

    db.session.commit()
