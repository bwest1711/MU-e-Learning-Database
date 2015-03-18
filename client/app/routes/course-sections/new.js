import Ember from 'ember';

export default Ember.Route.extend({
  model: function() {
    return {
      instructors: this.store.find('instructor'),
      courses: this.store.find('course'),
      courseVersions: this.store.find('courseVersion')
    };
  }
});
