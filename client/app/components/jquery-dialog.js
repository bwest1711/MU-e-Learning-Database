import Ember from 'ember';

export default Ember.Component.extend({
	className: 'has-dialog',
	_enableDataTable: function () {
		this.$('.dialog', this.$()).dialog();
	}.on( 'didInsertElement' )
});
