import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr('string'),
  abbreviation: DS.attr('string'), 
  administrator: DS.attr('string'),
  administratorEmail: DS.attr('string')
});
