import Ember from 'ember';

// Get a helper function to determine each circle's class.
// Unfortunately, we can't call helper functions from within the {{bind-attr}}
// helper, so instead we create a computed property for each circle that
// lets it know whether it is active or not
function getStageHelper(currStage) {
	return function () {
		var stg = this.get('stage');
		if (stg === currStage) { 
			return "circle-highlight"; 
		} else if (stg > currStage) {
			return "circle-done";
		} else {
			return "circle-todo";
		}
	};
}

export default Ember.Component.extend({
	stage: 0,
	certifyChecked: false,

	stage1Class: (getStageHelper(0)).property('stage'),
	stage2Class: (getStageHelper(1)).property('stage'),
	stage3Class: (getStageHelper(2)).property('stage'),
	stage4Class: (getStageHelper(3)).property('stage'),
	stage5Class: (getStageHelper(4)).property('stage'),

	onStage1: function () { return this.get('stage') === 0; }.property('stage'),
	onStage2: function () { return this.get('stage') === 1; }.property('stage'),
	onStage3: function () { return this.get('stage') === 2; }.property('stage'),
	onStage4: function () { return this.get('stage') === 3; }.property('stage'),
	onStage5: function () { return this.get('stage') === 4; }.property('stage'),

	actions: {
		next: function () {
			this.sendAction('saveNote', this.get('stage'));
			this.set('stage', this.get('stage') + 1);
			this.sendAction('updateReview', this.get('stage'));
			Ember.$(".note").val("");
			Ember.$("#signeeBox").val("");
			this.set('certifyChecked', false);

		},
		finish: function () {
			this.sendAction();
		}
	}
});
