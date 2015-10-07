import Ember from 'ember';

export default Ember.Component.extend({
	className: 'has-datatable',
	_enableDataTable: function () {
		this.$('.table', this.$()).dataTable();
	}.on( 'didInsertElement' )
});
