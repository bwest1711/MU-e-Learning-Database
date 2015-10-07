import Ember from 'ember';

export default Ember.Route.extend({
  model: function() {
    return Ember.RSVP.hash({ 
      courseVersions: this.store.findAll('courseVersion'),
      instructors: this.store.findAll('instructor'),
      departments: this.store.findAll('department'),
      courses: this.store.findAll('course')
    });
  }
});
