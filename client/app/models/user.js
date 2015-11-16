import DS from 'ember-data';

export default DS.Model.extend({
	fullName: DS.attr('string'),
	email: DS.attr('string'),
	uniqueid: DS.attr('string'),
	accessLevel: DS.attr('number')
});