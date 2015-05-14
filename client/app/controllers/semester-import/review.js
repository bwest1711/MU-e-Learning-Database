import Ember from 'ember';

export default Ember.ObjectController.extend({
  queryParams: ["semester", "year"],
  semester: null,
  year: null
});
