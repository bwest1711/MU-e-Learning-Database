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

  fullLabel: function () {
    var self = this;
    var course = this.get("course");

    // Combining computed properties with async relationships is really painful, but
    // there doesn't seem to be any better way to do it than this. 
    course.then(function (value) {
      var courseDept = value.get("department").get("abbreviation");
      var courseNumber = value.get("number");
      self.set("fullLabel", courseDept + courseNumber + " \"" + self.get("labelDisplay") + "\"");
    });
  }.property(),

  labelDisplay: function () {
    if(this.get("label") === "") {
      return "Unlabeled version";
    } else {
      return this.get("label");
    }
  }.property("label"),

  neverReviewed: function () {
    return this.get("qualityReviews").get("length") === 0;
  }.property("qualityReviews.@each.length"),

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

  dueForReview: function () {
    var latestDate = this.get("latestReview");

    // Milliseconds in three years, the specified 'past due' time
    // (TODO Make this configurable and put it in a better place)
    var maxTimeDiffMillis = 1000*60*60*24*365*3;

    return (Date.now() - latestDate.getTime() > maxTimeDiffMillis);
  }.property("latestReview")
});
