import Ember from 'ember';

var Router = Ember.Router.extend({
});

Router.map(function() {
  this.route("search");

  this.resource("courses", function() {
    this.route("new");
  });
  this.resource("course", { path: "/courses/:course_id" });

  this.resource("instructors", function() {
    this.route("new");
  });
  this.resource("instructor", { path: "/instructors/:instructor_id" });

  this.resource("courseVersions", function() {
    this.route("new");
  });
  this.route("courseVersion", { path: "/courseVersions/:courseVersion_id" }, function() {
    this.route("qualityReview", {resetNamespace: true, path: "/qualityReviews/:qualityReview_id"}, function(){
      this.route('view');
    });
  });

  this.resource("courseSections", function () {
    this.route("new");
  });
  this.resource("courseSection", { path: "/courseSections/:section_id" });

  this.route("tools");

  this.resource("departments", function() {
    this.route("new");
  });

  this.resource("instructions", function() {});

  this.route("help");

  this.route("semesterImport", function () {
    this.route("select");
    this.route("review");
    this.route("date");
  });

  this.route("semester-import", function() {
    this.route("done");
  });
  this.route('adminPanel');
});

export default Router;
