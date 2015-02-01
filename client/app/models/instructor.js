import DS from 'ember-data';

export default DS.Model.extend({
  full_name: DS.attr('string'),
  email: DS.attr('string'),
  courseVersions: DS.hasMany('courseVersion'),
  courseSections: DS.hasMany('courseSection')
});
