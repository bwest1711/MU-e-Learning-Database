from flask import request, abort

import requests
import xml.etree.ElementTree as ET

from api.models.instructor import Instructor
from api.models.course import Course
from api.models.course_version import CourseVersion
from api.models.course_section import CourseSection
from api.models.quality_review import QualityReview
from api.models.department import Department

# Banner encodes semesters (Fall, Winter, Spring, Summer) as integers
SEMESTER_MAP = { 'F': '10', 'W': '15', 'S': '20', 'U': '30' }

# Format string of the URL to retrieve the Banner import from
BANNER_URL = "http://ws.miamioh.edu/courseSectionV2/{year}{semester}.xml?offset={offset}"

# List of section attribute codes that indicate that the section is online
ONLINE_CODES = ["ONL", "HYB"]

# TODO the closure nonsense isnt necessary
def course_importer(db):

    def get_banner_courses():
        year = request.args.get('year')
        semester = request.args.get('semester')

        # Transform the semester parameter to its integer representation
        if semester not in SEMESTER_MAP.keys():
            abort(400)
        else:
            semester = SEMESTER_MAP[semester]

        sections = get_filtered_sections(year, semester)

        departments, courses, instructors = extract_objects(sections)

        print("\n".join("{} - {}".format(a, t) for (a, t) in departments))
        print("\n".join("{} - {}".format(a, t) for (a, t, c, x) in courses))
        print("\n".join("{} - {}".format(a, t) for (a, t) in instructors))

        # TODO return this as a bunch of json

        return "Total sections: [{}]".format(len(sections))

    return get_banner_courses

def extract_objects(sections):
    """ Extract domain objects from a list of sections """

    # Find all unique departments, courses, and instructors
    departments = {
        (s.findtext('courseSubjectCode'), s.findtext('deptName'))
        for s in sections
    }
    courses = {
        (s.findtext('courseSubjectCode'), s.findtext('courseNumber'), 
         s.findtext('courseTitle'), s.findtext('.//username'))
        for s in sections
    }
    instructors = {
        (s.findtext('.//username'), s.findtext('.//nameSortedInformal'))
        for s in sections
    }

    print("Before: {} depts, {} courses, {} instrs".format(
        len(departments), len(courses), len(instructors)))

    dept_exists = lambda d: (
        Department.query.filter(Department.abbreviation == d[0]).count() > 0)

    course_exists = lambda c: (
        Course.query.filter( Course.title == c[2] ).count() > 0)

    instructor_exists = lambda i: (
        Instructor.query.filter( Instructor.uniqueid == i[0] ).count() > 0)


    departments = [ d for d in departments if not dept_exists(d)       ] 
    courses =     [ c for c in courses     if not course_exists(c)     ] 
    instructors = [ i for i in instructors if not instructor_exists(i) ] 

    print("After: {} depts, {} courses, {} instrs".format(
        len(departments), len(courses), len(instructors)))

    return departments, courses, instructors


def get_filtered_sections(year, semester):
    """ Get a list of relevant sections (as XML Elements) from Banner """
    base_tree = None
    section_offset = 0
    total_sections = float('inf') # (lets the 1st iteration of the loop run)

    print("Getting parts: ")
    while section_offset < total_sections:
    #while section_offset < 3000:
        print("{}".format(section_offset))
        part_tree = get_banner_xml(year, semester, section_offset)

        if base_tree == None:
            base_tree = part_tree
            total_sections = int(part_tree.attrib['total'])
        else:
            for section in part_tree.iter('courseSection'):
                base_tree.append(section)

        section_offset += int(part_tree.attrib['count'])

    # Filter out sections that we aren't concerned with
    section_is_online = lambda s: any([t == "ONL" or t == "HYB" for t in s.itertext()])
    section_at_oxford = lambda s: s.findtext('campusCode') == "O"
    sections = [s for s in list(base_tree)
                if section_is_online(s)
                and section_at_oxford(s)]

    return sections


def get_banner_xml(year, semester, offset):
    """ Retrieve an XML document from BannerWeb """
    url = BANNER_URL.format(year=year, semester=semester, offset=offset)
    xml_req = requests.get(url)
    return ET.fromstring(xml_req.text)
