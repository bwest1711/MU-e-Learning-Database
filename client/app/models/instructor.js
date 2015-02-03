import DS from 'ember-data';

export default DS.Model.extend({
  fullName: DS.attr('string'),
  email: DS.attr('string'),
  courseVersions: DS.hasMany('courseVersion', { async: true }),
  courseSections: DS.hasMany('courseSection', { async: true })
});
