import DS from "ember-data";

export default DS.Model.extend({
  course: DS.belongsTo("course", { async: true }),
  instructor: DS.belongsTo("instructor", { async: true }),
  label: DS.attr("string"),
  courseType: DS.attr("string"),
  copyrightCompliant: DS.attr("boolean"),
  adaCompliant: DS.attr("boolean"),
  adaYear: DS.attr("number"),

  courseSections: DS.hasMany("courseSection", { async: true }),
  qualityReviews: DS.hasMany("qualityReview", { async: true }),

  // e.g.: CJS 111 "Intro to Criminal Justice"
  fullLabel: function () {
    var abbreviation = this.get("course").get("department").get("abbreviation");
    var number = this.get("course").get("number");
    var label = this.get("labelDisplay");

    return abbreviation + " " + number + " \"" + label + "\"";
  }.property("course.department.abbreviation", "course.number", "labelDisplay"),

  // Helper to avoid displaying a course with no label as "blank"
  labelDisplay: function () {
    if(this.get("label") === "") {
      return "Unlabeled version";
    } else {
      return this.get("label");
    }
  }.property("label"),

  // Whether or not the course version has ever been reviewed
  neverReviewed: function () {
    return this.get("qualityReviews").get("length") === 0;
  }.property("qualityReviews.@each.length"),

  // Date of the latest review of this course version
  latestReview: function () {
    var qrs = this.get("qualityReviews");
    var latestDate = new Date(0);

    qrs.forEach(function (item) {
      var thisDate = item.get("startDate");
      if (thisDate > latestDate) {
        latestDate = thisDate;
      }
    });
    return latestDate;
  }.property("qualityReviews.@each.endDate"),

  // Date that this course is due for review on (hard-coded to three years from last review)
  dueForReviewDate: function () {
    var latestDate = this.get("latestReview");
    var threeYearsMillis = 1000*60*60*24*365*3;

    return new Date(latestDate.getTime() + threeYearsMillis);
  }.property("latestReview"),

  dueForReview: function () {
    return Date.now() > this.get("dueForReviewDate");
  }.property("dueForReviewDate")
});
