import Ember from 'ember';

export default Ember.ObjectController.extend({
  courseTypes: ["Online Only", "Hybrid", "IVDL", "Face-to-Face Enhanced"],
  actions: {
    create: function () {
      var record = this.store.createRecord("courseVersion", {
        label: this.get("versionLabel"),
        instructor: this.get("selectedAuthor"),
        course: this.get("selectedCourse"),
        courseType: this.get("versionType"),
        copyrightCompliant: this.get("versionCopyrightCompliant"),
        adaCompliant: this.get("versionAdaCompliant")
      });
      record.save();
      this.transitionToRoute("courseVersions.index");
    }
  }
});
