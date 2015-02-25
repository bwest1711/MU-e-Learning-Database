import Ember from 'ember';

export function toShortDate(input) {

  if(input) {
    return input.toDateString();
  } else {
    return "";
  }
}

export default Ember.Handlebars.makeBoundHelper(toShortDate);
