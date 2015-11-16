import DS from 'ember-data';

export default DS.Model.extend({
	qualityReview: DS.belongsTo('qualityReview', { async: true }),
	stage: DS.attr('string'),
	text: DS.attr('string'),
	signature: DS.attr('string')
});