import Ember from 'ember';

export default Ember.Route.extend({
  queryParams: {
    title: {
      refreshModel: false
    }
  },
  model: function() {
    return Ember.RSVP.hash({
      courses: this.store.findAll("course"),
      departments: this.store.findAll("department"),
      instructors: this.store.findAll("instructor"),
      courseVersions: this.store.findAll("courseVersion"),
      courseSections: this.store.findAll("courseSection")
    });
  }
});
