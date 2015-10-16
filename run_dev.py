#!/usr/bin/python
'''Flask app runner for dev'''

from main import create_app

app = create_app()
app.config.from_object('config.Development')

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True, use_reloader=True)
