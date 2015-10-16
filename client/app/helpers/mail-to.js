import Ember from 'ember';

export default Ember.Helper.extend({
	compute(params, hash) {
		var _email = Ember.Handlebars.Utils.escapeExpression(params[0]);
		var _label = (params.length != 2) ? _email : Ember.Handlebars.Utils.escapeExpression(params[1]);

		var _link = '<a href="mailto:' + _email + '">' + _label + '</a>';
  		return new Ember.Handlebars.SafeString(_link);
	}
});