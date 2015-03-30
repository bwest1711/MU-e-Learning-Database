import Ember from 'ember';

export default Ember.ObjectController.extend({

  // Enable/disable 'certify' button based on checkbox status
  check1: false,
  check2: false,
  check3: false,
  allBoxesChecked: function () {
    return (
      this.get("check1") && 
      this.get("check2") && 
      this.get("check3") );
  }.property("check1", "check2", "check3"),

  actions: {
    deleteModel: function () {
      if (confirm("Are you sure you wish to delete this course section?")) {
        this.get("model").deleteRecord();
        this.get("model").save();
        this.transitionToRoute("courseSections");
      }
    },

    // Control the appearance of the section certification box
    startAttest: function () {
      this.set("attesting", true);
    },
    cancelAttest: function () {
      this.set("attesting", false);
    },
    saveAttest: function () {
      this.set("attested", true);
      this.set("attestedDate", new Date());
      this.set("attestedSignee", this.get("signee"));
      this.set("attesting", false);
      this.model.save();
    }
  }
});
