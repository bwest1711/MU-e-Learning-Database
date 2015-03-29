import Ember from "ember";

export default Ember.ObjectController.extend({
  isUnderReview: false,
  actions: {
    saveModel: function () {
      this.get("model").save();
    },
    deleteModel: function () {
      if (confirm("Are you sure you wish to delete this course version?")) {
        this.get("model").deleteRecord();
        this.get("model").save();
        this.transitionToRoute("courseVersions");
      }
    },
    startReview: function () {
      this.set("isUnderReview", true);
    },
    finalizeReview: function () {
      this.set("isUnderReview", false);
      var thisModel = this.get("model");
      var newReview = this.store.createRecord("qualityReview", {
        courseVersion: thisModel,
        startDate: new Date(),
        endDate: new Date(),
        stage: "Complete"
      });
      newReview.save();
    }
  }
});
