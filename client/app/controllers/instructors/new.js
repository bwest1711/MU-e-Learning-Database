import Ember from "ember";

export default Ember.ObjectController.extend({
  actions: {
    create: function () {
      var instructor = this.store.createRecord("instructor", {
        fullName: this.get("fullName"),
        email: this.get("email"),
        uniqueid: this.get("uniqueid")
      });
      instructor.save();

      // Clean-up fields that were just used
      this.set("fullName", "");
      this.set("email", "");
      this.set("uniqueid", "");

      this.transitionToRoute("instructors.index");
    }
  }
});
