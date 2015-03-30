import Ember from 'ember';

export default Ember.ObjectController.extend({

  sortedCourseVersions: function () {
  }.property("courseVersions.@each"),

  actions: {
    create: function () {
      var record = this.store.createRecord("courseSection", {
        courseVersion: this.get("selectedCourseVersion"),
        instructor: this.get("selectedInstructor"),
        semester: this.get("sectionSemester"),
        crn: this.get("sectionCRN")
      });
      record.save();
      this.transitionToRoute("courseSections.index");
    }
  }
});
