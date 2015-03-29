import Ember from 'ember';

export default Ember.Route.extend({
  model: function () {
    return {
      departments: this.store.find("department")
    }
  }
});
