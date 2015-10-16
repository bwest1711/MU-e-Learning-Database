import Ember from 'ember';

export default Ember.Component.extend({
	className: 'has-datatable',
	_enableDataTable: function () {
		this.$('.table', this.$()).dataTable({
			    dom: 'Bfrt',
			    buttons: [
			        'excel'
			    ],
			    columns: [
				    { "type": "html" },
				    { "type": "html" },
				    { "type": "html" },
				    { "type": "html" },
				    { "type": "html" },
				    { "type": "html" }
				]
		});
	}.on( 'didInsertElement' )
});
