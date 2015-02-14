import Ember from 'ember';

export default Ember.Route.extend({
  queryParams: {
    title: {
      refreshModel: false
    }
  },
  model: function() {
    return {
      instructors: this.store.find('instructor'),
      courseVersions: this.store.find('courseVersion')
    };
  }
});
