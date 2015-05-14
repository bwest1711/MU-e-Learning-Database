import Ember from 'ember';

export default Ember.Route.extend({
  queryParams: {
    category: {
      refreshModel: true
    }
  },
  model: function (params) {
    console.log("Starting Banner import for "+params.semester+" "+params.year);
    return Ember.$.getJSON("/api/banner_import?semester="+params.semester+"&year="+params.year);
  },
  setupController: function (controller, model) {
    console.log("Setting up controller");
    controller.set("departments", model.departments);
    controller.set("courses", model.courses);
    controller.set("instructors", model.instructors);
    controller.set("courseSections", model.course_sections);
    console.log("done");
  }
});
