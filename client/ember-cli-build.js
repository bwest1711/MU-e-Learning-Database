var EmberApp = require('ember-cli/lib/broccoli/ember-app');

module.exports = function(defaults) {
    var app = new EmberApp(defaults, {

    });

    app.import('bower_components/bootstrap/dist/css/bootstrap.min.css');
	app.import('bower_components/bootstrap/dist/js/bootstrap.min.js');
	app.import('bower_components/bootstrap/dist/fonts/glyphicons-halflings-regular.woff', {
	  destDir: 'fonts'
	});
	app.import('bower_components/bootstrap/dist/fonts/glyphicons-halflings-regular.woff2', {
	  destDir: 'fonts'
	});
	app.import('vendor/DataTables/datatables.min.js');
	app.import('vendor/DataTables/datatables.min.css');
	app.import('bower_components/jquery-ui/jquery-ui.min.js');
	app.import('bower_components/jquery-ui/themes/base/jquery-ui.min.css');

	app.import('vendor/overrides/datatables.css');

	return app.toTree();
};