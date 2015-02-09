import Ember from 'ember';

export default Ember.Controller.extend({
  actions: {
    search: function() {
      // TODO uhh
      var queryObj = {
        'filters': [
          {'name': 'fullName', 'op': 'like', 'val': '%petyr%'}
        ]
      };
      var queryString = '?q=' + JSON.stringify(queryObj);
      var endpoint = '/api/instructors';
      $.getJSON(endpoint + queryString, function(data) {
        alert(JSON.stringify(data));
      });
    }
  }
});
