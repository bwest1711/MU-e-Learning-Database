import Ember from 'ember';

export default Ember.Controller.extend({
  actions: {
    deleteModel: function () {
      if (confirm("Are you sure you wish to delete this instructor?")) {
        this.get("model").deleteRecord();
        this.get("model").save();
        this.transitionToRoute("instructors");
      }
    }
  }
});
