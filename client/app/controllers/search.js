import Ember from 'ember';

export default Ember.ObjectController.extend({
  queryParams: ['title'],
  title: "",

  filteredCourses: function () {
    var courseVersions = this.get('courseVersions');
    var searchTitle = this.get('title');

    if (searchTitle !== "") {
      courseVersions = courseVersions.filter(function(item, index, self) {
        return item.get('course').get('title').toLowerCase().indexOf(searchTitle.toLowerCase()) > -1;
      });
    }
    return courseVersions;
  }.property('title'),

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
