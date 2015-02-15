import Ember from 'ember';

export default Ember.ObjectController.extend({
  actions: {
    saveModel: function () {
      this.get('model').save();
      alert('saved model');
    },
    deleteModel: function() {
      this.get('model').deleteRecord();
      this.get('model').save();
      alert('deleted record');
    }
  }
});
