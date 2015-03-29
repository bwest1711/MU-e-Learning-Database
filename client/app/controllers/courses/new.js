import Ember from 'ember';

export default Ember.ObjectController.extend({
  actions: {
    create: function () {
      var record = this.store.createRecord("course", {
        department: this.get("selectedDepartment"),
        number: this.get("courseNumber"),
        title: this.get("courseTitle"),
      });
      record.save();
      this.transitionToRoute("courses.index");
    }
  }
});
