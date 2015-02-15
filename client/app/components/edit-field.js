import Ember from 'ember';

export default Ember.Component.extend({
  editing: false,
  actions: {
    startEdit: function () {
      this.set('editing', true);
    },
    saveEdit: function () {
      this.set('editing', false);
      this.sendAction();
    },
    cancelEdit: function () {
      this.set('editing', false);
    }
  }
});
