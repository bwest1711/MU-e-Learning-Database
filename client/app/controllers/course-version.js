import Ember from "ember";

export default Ember.Controller.extend({
  isUnderReview: false,
  curReview: 0,
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
      var self = this;
      this.set("isUnderReview", true);
      var thisModel = this.get("model");
      var newReview = this.store.createRecord("qualityReview", {
        courseVersion: thisModel,
        startDate: new Date(),
        endDate: null,
        stage: 0
      });
      newReview.save().then(function(response) {
        console.log(response.get('id'));
        self.set('curReview', response.get('id'));
      }, function(response) {
        console.log(response);
      });
    },
    updateReview: function(stage) {
      var thisModel = this.get('model');
      var record = this.store.findRecord('qualityReview', this.get('curReview'));
      console.log(record);
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
    },
    saveNote: function(stage) {
      var self = this;
      var text =  Ember.$('.note').val();
      var signature =  Ember.$('#signeeBox').val()
      self.store.findRecord('qualityReview', this.get('curReview')).then(function(qualityReview){
        var note = self.store.createRecord('note', {
          stage: stage,
          qualityReview: qualityReview,
          text: text,
          signature: signature
        });
        note.save();
      });
      // console.log(thisModel.get('id'));
      // var note = this.store.createRecord('note', {
      //   stage: stage,
      //   qualityReview: thisModel,
      //   text:  Ember.$('.note').val(),
      //   signature: Ember.$('#signeeBox').val()
      // });
      // note.save();
    }
  }
});
