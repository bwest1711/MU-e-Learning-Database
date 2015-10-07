import Ember from 'ember';

export default Ember.Route.extend({
  model: function() {
    return {
      instructors: this.store.findAll('instructor'),
      courses: this.store.findAll('course')
    };
  }
});
