import Ember from 'ember';

export default Ember.ObjectController.extend({
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
  selectedYear: null
});
