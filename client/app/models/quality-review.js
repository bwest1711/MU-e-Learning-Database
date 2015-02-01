import DS from 'ember-data';

export default DS.Model.extend({
  courseVersion: DS.belongsTo('courseVersion'),
  stage: DS.attr('string')
});
