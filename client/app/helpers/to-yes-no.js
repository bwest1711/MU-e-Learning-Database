import Ember from 'ember';

export function toYesNo(input) {
  return input ? "Yes" : "No";
}

export default Ember.Handlebars.makeBoundHelper(toYesNo);
