import DS from 'ember-data';

export default DS.Model.extend({
  courseVersion: DS.belongsTo('course'),
  instructor: DS.belongsTo('instructor'),
  semester: DS.attr('string')
});
