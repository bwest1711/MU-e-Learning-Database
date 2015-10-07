import Ember from 'ember';

export default Ember.Controller.extend({

  queryParams: ['title'],
  title: "",

  // Text values for different search types (can't use an enum here)
  courseTypes: ["Online Only", "Hybrid", "IVDL", "Face-to-Face Enhanced"],

  // Whether versions or sections are being searched
  searchingVersions: true,

  // Field values for version search
  searchVersionInstructor: null,
  searchVersionDepartment: null,
  searchVersionCourse: null,
  searchVersionType: null,
  searchVersionTitle: "",
  searchVersionDueForReview: null,
  searchVersionCopyCompliant: null,
  searchVersionADACompliant: null,

  // Field values for section search
  searchSectionInstructor: null,
  searchSectionDepartment: null,
  searchSectionCourse: null,
  searchSectionType: null,
  searchSectionCRN: "",
  searchSectionSemester: "",
  searchSectionAttested: null,

  // (Yes, this is bad, needs refactoring, etc. if time constraints allow)
  // (It works "well enough" and it's not in need of frequent change)
  filteredCourses: function () {
    var courseVersions = this.get("model.courseVersions");
    console.log(courseVersions);
    var courseSections = this.get("model.courseSections");

    var searchingVersions = this.get("searchingVersions"), 
        searchVersionInstructor = this.get("searchVersionInstructor"),
        searchVersionDepartment = this.get("searchVersionDepartment"),
        searchVersionCourse = this.get("searchVersionCourse"),
        searchVersionType = this.get("searchVersionType"),
        searchVersionTitle = this.get("searchVersionTitle"),
        searchVersionDueForReview = this.get("searchVersionDueForReview"),
        searchVersionCopyCompliant = this.get("searchVersionCopyCompliant"),
        searchVersionADACompliant = this.get("searchVersionADACompliant"),
        searchSectionInstructor = this.get("searchSectionInstructor"),
        searchSectionDepartment = this.get("searchSectionDepartment"),
        searchSectionCourse = this.get("searchSectionCourse"),
        searchSectionType = this.get("searchSectionType"),
        searchSectionCRN = this.get("searchSectionCRN"),
        searchSectionSemester = this.get("searchSectionSemester"),
        searchSectionAttested = this.get("searchSectionAttested");

    // Filters for course versions
    if (searchVersionTitle !== "") {
      courseVersions = courseVersions.filter(function(item) {
        return item.get("course").get("title").toLowerCase()
          .indexOf(searchVersionTitle.toLowerCase()) > -1;
      });
    }
    if (searchVersionInstructor) {
      courseVersions = courseVersions.filter(function(item) {
        return item.get("instructor").get("id") === searchVersionInstructor;
      });
    }
    if (searchVersionDepartment) {
      courseVersions = courseVersions.filter(function(item) {
        return item.get("course").get("department").get("id") === searchVersionDepartment;
      });
    }
    if (searchVersionCourse) {
      courseVersions = courseVersions.filter(function(item) {
        return item.get("course").get("id") === searchVersionCourse;
      });
    }
    if (searchVersionType) {
      courseVersions = courseVersions.filter(function(item) {
        return item.get("courseType") === searchVersionType;
      });
    }
    if (searchVersionCopyCompliant != null) {
      courseVersions = courseVersions.filter(function(item) {
        return item.get("copyrightCompliant") === searchVersionCopyCompliant;
      });
    }
    if (searchVersionADACompliant != null) {
      courseVersions = courseVersions.filter(function(item) {
        return item.get("adaCompliant") === searchVersionADACompliant;
      });
    }
    if (searchVersionDueForReview != null) {
      courseVersions = courseVersions.filter(function(item) {
        return item.get("dueForReview") === searchVersionDueForReview;
      });
    }

    // Filters for course sections
    if (searchSectionInstructor) {
      courseSections = courseSections.filter(function(item) {
        return item.get("instructor").get("id") === searchSectionInstructor;
      });
    }
    if (searchSectionDepartment) {
      courseSections = courseSections.filter(function(item) {
        return item.get("courseVersion").get("course").get("department").get("id") === searchSectionDepartment;
      });
    }
    if (searchSectionCourse) {
      courseSections = courseSections.filter(function(item) {
        return item.get("courseVersion").get("course").get("id") === searchSectionCourse;
      });
    }
    if (searchSectionType) {
      courseSections = courseSections.filter(function(item) {
        return item.get("courseVersion").get("course").get("courseType") === searchSectionType;
      });
    }
    if (searchSectionCRN !== "") {
      courseSections = courseSections.filter(function(item) {
        return item.get("crn").indexOf(searchSectionCRN) > -1;
      });
    }
    if (searchSectionSemester !== "") {
      courseSections = courseSections.filter(function(item) {
        return item.get("semester").toLowerCase()
          .indexOf(searchSectionSemester.toLowerCase()) > -1;
      });
    }
    if (searchSectionAttested != null) {
      courseSections = courseSections.filter(function(item) {
        return item.get("attested") === searchSectionAttested;
      });
    }

    if (searchingVersions) {
      return courseVersions;
    } else {
      return courseSections;
    }
  }.property(
    // New search is triggered when any search field changes
    "searchingVersions", 

    "searchVersionTitle",
    "searchVersionInstructor",
    "searchVersionDepartment",
    "searchVersionCourse",
    "searchVersionType",
    "searchVersionDueForReview",
    "searchVersionCopyCompliant",
    "searchVersionADACompliant",

    "searchSectionInstructor",
    "searchSectionDepartment",
    "searchSectionCourse",
    "searchSectionType",
    "searchSectionCRN",
    "searchSectionSemester",
    "searchSectionAttested"
  )
});
