import Ember from 'ember';

export default Ember.ObjectController.extend({
  isUnderReview: false,
  actions: {
    saveModel: function () {
      this.get('model').save();
    },
    deleteModel: function () {
      this.get('model').deleteRecord();
      this.get('model').save();
      this.transitionToRoute('courseVersions');
    },
    startReview: function () {
      this.set('isUnderReview', true);
    },
    finalizeReview: function () {
      this.set('isUnderReview', false);
    }
  }
});
