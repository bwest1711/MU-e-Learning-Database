################################################################################
# banner.py
#
# The purpose of this file is to import information about a semester's courses,
# instructors, departments, and sections from the Banner system into our own.
# It's best to think of it as a pipeline that filters and transforms the domain
# objects. It might be helpful to look at an example of the XML document that
# banner returns by visiting the following URL:
#
# http://ws.miamioh.edu/courseSectionV2/201515.xml?offset=0
#
# Things that might be useful to know: 
# - You'll need a good understanding of tuples, sets, dictionaries, list
#   comprehensions, and lambda functions to read this code
# - The Banner server only returns 1000 sections at a time, so you have to query
#   multiple times to get all sections
# - The Banner XML isn't relational, so you have to manually de-duplicate and
#   re-build the references to departments, instructors, etc.
# - The general pipeline for the data is this: 
#   (Giant XML blobs) -> (List of XML sections) -> (Domain object tuples) ->
#       (Tuples filtered by pre-existence) -> (Giant JSON response)
#
################################################################################

from flask import request, abort, jsonify

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

def get_banner_courses():
    """ Retrieve & parse a set of courses (et. al) of a given semester from Banner """

    year = request.args.get('year')
    semester = request.args.get('semester')

    # Make sure the semester code is a valid value
    if semester not in SEMESTER_MAP.keys():
        abort(400)
    else:
        semester = SEMESTER_MAP[semester]
    # Make sure the year code is a valid integer
    try:
        int(year)
    except ValueError:
        abort(400)

    # Extract domain objects from the associated XML document
    sections = get_xml_sections(year, semester)
    departments, courses, course_sections, instructors = filter_objects(
        *extract_xml_objects(sections))

    print("Returning {} depts., {} courses, {} sections, and {} instructors".format(
        len(departments), len(courses), len(course_sections), len(instructors)))

    return jsonify(**to_dict(departments, courses, course_sections, instructors))


def get_banner_xml(year, semester, offset):
    """ Retrieve an XML document from BannerWeb """
    url = BANNER_URL.format(year=year, semester=semester, offset=offset)
    xml_req = requests.get(url)
    return ET.fromstring(xml_req.text)


def get_xml_sections(year, semester):
    """ Get a list of relevant sections (as XML Elements) from Banner """
    base_tree = None
    section_offset = 0
    total_sections = float('inf') # (lets the 1st iteration of the loop run)

    print("Getting parts: ")
    while section_offset < total_sections:
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
    section_is_online = lambda s: any([t in ONLINE_CODES for t in s.itertext()])
    section_at_oxford = lambda s: s.findtext('campusCode') == "O"
    sections = [s for s in list(base_tree)
                if section_is_online(s)
                and section_at_oxford(s)]

    return sections


def extract_xml_objects(sections):
    """ Parse out departments, courses, and instructors from XML sections """

    # Note here that we use sets of tuples to guarantee uniqueness. While using
    # dictionaries with named fields might be more semantic, they can't be hashed,
    # and thus can't be stored in sets
    departments = {
        ( 
            s.findtext('courseSubjectCode'), 
            s.findtext('deptName') 
        ) 
        for s in sections
    }
    courses = {
        (
            s.findtext('courseSubjectCode'), 
            s.findtext('courseNumber'), 
            s.findtext('courseTitle')
        )
        for s in sections
    }
    course_sections = {
        (
            s.findtext('.//username'),
            s.findtext('courseTitle')
        )
        for s in sections
    }
    instructors = {
        (
            s.findtext('.//username'), 
            s.findtext('.//nameSortedInformal')
        )
        for s in sections
    }

    return departments, courses, course_sections, instructors


def filter_objects(departments, courses, course_sections, instructors):
    """ Extract domain objects from a list of sections """

    print("Before: {} depts, {} courses, {} instrs".format(
        len(departments), len(courses), len(instructors)))

    # Filter out objects that already exist in the DB, or objects that have
    # "None" as a field (indicating a malformed section from the XML doc)

    # (referencing tuple fields by index e.g. d[0] is ugly, but again, we need
    # to utilize them for uniqueness)
    dept_exists = lambda d: (
        Department.query.filter(Department.abbreviation == d[0]).count() > 0)

    course_exists = lambda c: (
        Course.query.filter( Course.title == c[2] ).count() > 0)

    instructor_exists = lambda i: (
        Instructor.query.filter( Instructor.uniqueid == i[0] ).count() > 0)

    contains_null = lambda t: any([i is None for i in t])

    departments = [ d for d in departments 
                    if not dept_exists(d) and not contains_null(d) ] 
    courses =     [ c for c in courses     
                    if not course_exists(c) and not contains_null(c) ] 
    instructors = [ i for i in instructors 
                    if not instructor_exists(i) and not contains_null(i) ] 
    course_sections = [ cs for cs in course_sections if not contains_null(cs) ]

    print("After: {} depts, {} courses, {} instrs".format(
        len(departments), len(courses), len(instructors)))

    return departments, courses, course_sections, instructors


def to_dict(depts, courses, course_sections, instructors):
    """ Transform the entire collection into a single JSON-ifiable dict """

    department_to_dict = lambda d: {
        "abbreviation": d[0],
        "name": d[1]
    }
    course_to_dict = lambda c: {
        "department": c[0],
        "number": c[1],
        "title": c[2]
    }
    course_section_to_dict = lambda s: {
        "uniqueid": s[0],
        "title": s[1]
    }
    instructor_to_dict = lambda i: {
        "uniqueid": i[0],
        "fullName": i[1]
    }

    return {
        "departments": [department_to_dict(d) for d in depts],
        "courses": [course_to_dict(c) for c in courses],
        "course_sections": [course_section_to_dict(s) for s in course_sections],
        "instructors": [instructor_to_dict(i) for i in instructors]
    }
