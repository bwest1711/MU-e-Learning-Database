import Ember from 'ember';

export default Ember.ObjectController.extend({
  queryParams: ['title'],
  title: "",

  filteredCourseVersions: function() {
    var self = this;

    var filters = [
      { "name": "label", "op": "like", "val": "%" + this.get('title') + "%" }
    ];

    var search = Ember.$.ajax({
      url: "http://localhost:5000/api/courseVersions",
      data: { "q": JSON.stringify( { "filters": filters } ) },
      dataType: "json",
      contentType: "application/json"
    });

    search.success(function(data) { 
      self.set('courseVersions', data.courseVersions);
      alert(JSON.stringify(self.get('courseVersions')));
    });

  }.property('title'),

  actions: {
  }

});
