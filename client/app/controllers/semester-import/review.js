import Ember from 'ember';

export default Ember.ObjectController.extend({
  queryParams: ["semester", "year"],
  semester: null,
  year: null,

  dueDate: null,

  departments: [],
  courses: [],
  instructors: [],
  courseSections: [],

  actions: {
    finalizeImport: function () {
      if (confirm("Are you sure you wish to import the data listed? This cannot be undone.")) {
        this.transitionTo("semesterImport.done");
      }
    }
  }
});
