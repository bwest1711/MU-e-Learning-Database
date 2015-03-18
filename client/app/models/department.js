import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr('string'),
  abbreviation: DS.attr('string'), 
  admin: DS.attr('string'),
  adminEmail: DS.attr('string'),
  aliases: DS.attr('string'),
  division: DS.attr('string'),

  courses: DS.hasMany('course', { async: true })
});
