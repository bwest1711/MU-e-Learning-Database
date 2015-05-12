import Ember from 'ember';

export default Ember.Route.extend({
  model: function() {
    return { 
      courseVersions: this.store.find('courseVersion'),
      instructors: this.store.find('instructor'),
      departments: this.store.find('department'),
      courses: this.store.find('course')
    };
  }
});
