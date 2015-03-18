import Ember from 'ember';

export default Ember.ObjectController.extend({
  actions: {
    startAttesting: function () {
      this.set("attesting", true);
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