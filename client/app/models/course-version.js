import DS from 'ember-data';

export default DS.Model.extend({
  course: DS.belongsTo('course', { async: true }),
  instructor: DS.belongsTo('instructor', { async: true }),
  label: DS.attr('string'),
  courseSections: DS.hasMany('courseSection', { async: true }),
  qualityReviews: DS.hasMany('qualityReview', { async: true }),
  copyrightCompliant: DS.attr('boolean'),
  adaCompliant: DS.attr('boolean'),
  adaComplianceYear: DS.attr('number'),

  labelDisplay: function() {
    if(this.get('label') === '') {
      return 'Unlabeled version';
    } else {
      return this.get('label');
    }
  }.property('label')
});
