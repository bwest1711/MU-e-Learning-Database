import Ember from 'ember';

export default Ember.Helper.extend({
	compute(params, hash) {
		return params[0] ? "Yes" : "No";
	}
});