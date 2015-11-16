import DS from 'ember-data';

export default DS.Model.extend({
	courseVersion: DS.belongsTo('courseVersion', { async: true }),
	stage: DS.attr('string'),
	startDate: DS.attr('date'),
	endDate: DS.attr('date'),
	notes: DS.hasMany('note', { async: true })
});
