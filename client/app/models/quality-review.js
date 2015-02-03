import DS from 'ember-data';

export default DS.Model.extend({
  courseVersion: DS.belongsTo('courseVersion', { async: true }),
  stage: DS.attr('string')
});
