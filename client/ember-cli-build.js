var EmberApp = require('ember-cli/lib/broccoli/ember-app');
var Funnel   = require('broccoli-funnel');

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
	app.import('vendor/DataTables/datatables.js');
	app.import('vendor/DataTables/datatables.css');
	app.import('bower_components/jquery-ui/jquery-ui.min.js');
	app.import('bower_components/jquery-ui/themes/base/jquery-ui.min.css');

    var extraAssets = new Funnel('bower_components/jquery-ui/themes/base/images', {
 		srcDir: '/',
		include: ['*.png'],
		destDir: '/assets/images'
	});

	return app.toTree(extraAssets);
};