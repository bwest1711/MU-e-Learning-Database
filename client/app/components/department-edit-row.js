import Ember from "ember";

export default Ember.Component.extend({
  tagName: "tr",
  editing: false,
  actions: {
    confirmAndDelete: function () {
      if (window.confirm("Do you want to delete this department?")) {
        if (window.confirm("Are you sure? This may orphan the courses that are assigned to it.")) {
          this.get("dept").destroyRecord();
        }
      } 
    },
    startEdit: function () {
      this.set("editing", true);
    },
    saveEdit: function () {
      this.set("editing", false);
      this.get("dept").save();
      this.sendAction();
    },
    cancelEdit: function () {
      this.set("editing", false);
      this.get("dept").rollback();
    }
  }
});
