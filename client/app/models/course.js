import DS from 'ember-data';

export default DS.Model.extend({ 
  title: DS.attr('string'),
  department: DS.attr('string'),
  number: DS.attr('number'),
  courseVersions: DS.hasMany('courseVersion', { async: true }),

  display: function() {
    return this.get('department') + ' ' + this.get('number') + ' ' + this.get('title');
  }.property('title', 'department', 'number'),

  displayShort: function() {
    return this.get('department') + ' ' + this.get('number');
  }.property('department', 'number')
});
