## Miami University e-Learning Course Database

Repository for Miami University's online course database, for use by the Advanced Learning Technologies group. 

* Backend API written in Python using Flask-Restful (/api directory)
* Frontend written in Javascript using Ember.js (/client directory)

Project structure based on [todo-flask-ember](https://github.com/gaganpreet/todo-flask-ember) by [Gaganpreet Singh Arora](https://github.com/gaganpreet).

## Setup

(Assuming Ubuntu ~12.x with Python installed.)

### Server-side

Clone the repo: 

    git clone https://github.com/mdchoate/MU-e-Learning-Database.git
    cd MU-e-Learning-Database

Install pip:

    apt-get install python-pip

Install virtualenv and create a local Python environment:

    apt-get install python-virtualenv
    virtualenv env

Change to newly-created environment:

    source env/bin/activate

Install dependencies using pip:

    pip install requirements.txt

Initialize the database and insert test data: 

    python init_db.py
    python insert_test_data.py

At this point, the API is ready to run. However, you should still build the client-side Ember app before running the server. 

### Client-side

Install the most recent versions of npm and node.js: 

    apt-add-repository ppa:chris-lea/node.js
    apt-get update
    apt-get install nodejs

Install ember-cli and bower:

    npm install -g ember-cli
    npm install -g bower

Change to 'client' directory and install dependencies:

    npm install
    bower install

Run the automatic builder (this will watch the folder for changes and re-build the client-side app if needed):

    ember build --watch

## Run

Once you have all dependencies installed, the client-side app built, and the database initialized, use one of the helper scripts to run the server (in the project's root directory): 

    python run_dev.py

The server should now be serving a page at http://localhost:5000/.
