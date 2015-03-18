import DS from 'ember-data';

export default DS.Model.extend({
  courseVersion: DS.belongsTo('courseVersion', { async: true }),
  instructor: DS.belongsTo('instructor', { async: true }),
  semester: DS.attr('string'),

  attested: DS.attr('boolean'),
  attestedDueDate: DS.attr('date'),
  attestedDate: DS.attr('date'),
  attestedSignee: DS.attr('string'),
});
