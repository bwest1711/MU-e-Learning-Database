var EmberApp = require('ember-cli/lib/broccoli/ember-app');

module.exports = function(defaults) {
    var app = new EmberApp(defaults, {
        // Any other options
    });

    app.import('bower_components/bootstrap/dist/css/bootstrap.min.css');
	app.import('bower_components/bootstrap/dist/js/bootstrap.min.js');
	app.import('bower_components/bootstrap/dist/fonts/glyphicons-halflings-regular.woff', {
	  destDir: 'fonts'
	});
	app.import('bower_components/bootstrap/dist/fonts/glyphicons-halflings-regular.woff2', {
	  destDir: 'fonts'
	});
	app.import('vendor/DataTables/datatables.js');
	app.import('vendor/DataTables/datatables.css');
    return app.toTree();
};