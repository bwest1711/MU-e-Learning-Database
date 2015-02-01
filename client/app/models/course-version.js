import DS from 'ember-data';

export default DS.Model.extend({
  courseId: DS.belongsTo('course'),
  instructorId: DS.belongsTo('instructor'),
  label: DS.attr('string'),
  courseSections: DS.hasMany('courseSection'),
  qualityReviews: DS.hasMany('qualityReview'),
  copyrightCompliant: DS.attr('boolean'),
  adaCompliant: DS.attr('boolean'),
  adaComplianceYear: DS.attr('number')
});
