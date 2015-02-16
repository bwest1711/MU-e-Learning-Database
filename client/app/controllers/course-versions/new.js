import Ember from 'ember';

export default Ember.ObjectController.extend({
  actions: {
    create: function () {
      var instructor;
      var course;
      var self = this;

      this.store.find('instructor', 1).then(function (value) {

        instructor = value;
        return self.store.find('course', 1);

      }).then(function (value) {

        course = value;

      }).then(function () {

        var record = self.store.createRecord('courseVersion', {
          label: self.get('label'),
          courseType: 'Online Only',
          instructor: instructor,
          course: course,
          adaCompliant: self.get('adaCompliant'),
          copyrightCompliant: self.get('copyrightCompliant'),
        });

        record.save();
      }).then(function () {
        self.transitionToRoute('courseVersions.index');
      });
    }
  }
});
