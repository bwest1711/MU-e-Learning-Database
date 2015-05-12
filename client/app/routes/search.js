import Ember from 'ember';

export default Ember.Route.extend({
  queryParams: {
    title: {
      refreshModel: false
    }
  },
  model: function() {
    return {
      courses: this.store.find("course"),
      departments: this.store.find("department"),
      instructors: this.store.find("instructor"),
      courseVersions: this.store.find("courseVersion"),
      courseSections: this.store.find("courseSection")
    };
  }
});
