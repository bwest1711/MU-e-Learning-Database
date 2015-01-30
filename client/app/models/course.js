import DS from 'ember-data';

export default DS.Model.extend({ 
  title: DS.attr('string'),
  department: DS.attr('string'),
  number: DS.attr('number')
});
