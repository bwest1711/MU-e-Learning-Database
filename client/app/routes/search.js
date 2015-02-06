import Ember from 'ember';

export default Ember.Route.extend({
  model: function() {
    return {
      instructors: this.store.find('instructor'),
      // TODO Replace this part with the *actual* search resource..
      courseVersions: this.store.find('courseVersion')
    };
  }
});
