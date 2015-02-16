import Ember from 'ember';

var Router = Ember.Router.extend({
});

Router.map(function() {
  this.route("search");

  this.resource("courses", function() {});
  this.resource("course", { path: '/courses/:course_id' });

  this.resource("instructors", function() {});
  this.resource("instructor", { path: '/instructors/:instructor_id' });

  this.resource("courseVersions", function() {
    this.route('new');
  });
  this.resource("courseVersion", { path: '/courseVersions/:courseVersion_id' });

  this.route("tools");
});

export default Router;
