import Ember from 'ember';

// Thanks to s.meijer @ StackOverflow
export function mailTo(emailAddress, label) {
  emailAddress = Ember.Handlebars.Utils.escapeExpression(emailAddress);
  label = (arguments.length === 2) ? emailAddress : Ember.Handlebars.Utils.escapeExpression(label);

  var link = '<a href="mailto:' + emailAddress + '">' + label + '</a>';
  return new Ember.Handlebars.SafeString(link);
}

export default Ember.Handlebars.makeBoundHelper(mailTo);
