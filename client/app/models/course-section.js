import DS from 'ember-data';

export default DS.Model.extend({
  courseVersion: DS.belongsTo('courseVersion', { async: true }),
  instructor: DS.belongsTo('instructor', { async: true }),
  semester: DS.attr('string')
});
