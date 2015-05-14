import Ember from 'ember';

export default Ember.ObjectController.extend({
  loading: false,

  semesterOptions: [
    { name: "Fall",   letter: "F" },
    { name: "Winter", letter: "W" },
    { name: "Spring", letter: "S" },
    { name: "Summer", letter: "U" }
  ],
  selectedSemester: null,

  yearOptions: function () {
    var years = [];
    for (var i = 2012; i < 2030; i++) {
      years.push(""+i);
    }
    return years;
  }.property(),
  selectedYear: null,

  actions: {
    startImport: function () {
      if (confirm("Are you sure you wish to begin importing? You *will* be able to review the imported data before it is added. The process may take several minutes.")) {
        this.set("loading", true);
        this.transitionTo("semesterImport.review", {
          queryParams: {
            semester: this.get("selectedSemester"),
            year: this.get("selectedYear")
          }
        });
      }
    }
  }
});
