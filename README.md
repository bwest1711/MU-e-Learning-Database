## Miami University e-Learning Course Database

Repository for Miami University's online-course management system, for use by the Advanced Learning Technologies group. Its purpose is to allow the ALT group to organize information about the university's online courses, including information about their compliance status, adherence to divisional standards, and review schedules. The project is implemented as a single-page JavaScript web application powered by a REST API. 

* Backend API written in Python using Flask (`/api` directory)
* Frontend written in Javascript using Ember.js (`/client` directory)

### Maintainers

New contributors and maintainers of the project should read the included `NOTES_TO_MAINTAINERS.md` file for more useful information about its implementation. 

## Setup

(Assuming Ubuntu ~12.x or CentOS 7 with Python installed. Root privileges may be necessary to run some commands.)

### Server-side

Clone the repo: 

    git clone https://github.com/mdchoate/MU-e-Learning-Database.git
    cd MU-e-Learning-Database

Install pip:

    # Ubuntu
    apt-get install python-pip
    # CentOS / RHEL
    yum install -y epel-release 
    yum install -y python-pip

Install virtualenv and create a local Python environment:

    # Ubuntu
    apt-get install python-virtualenv
    # CentOS / RHEL
    yum install -y python-virtualenv

    virtualenv env

Change to newly-created environment:

    source env/bin/activate

Install dependencies using pip:

    pip install -r requirements.txt

Patch one of the dependencies to work with Ember.js (required):

    ./fix_flask_restful.sh

Install PostgreSQL:
    # Ubuntu
    apt-get install postgresql
    # CentOS / RHEL
    yum install -y postgresql

Initialize the database and insert test data: 

    env/bin/python init_db.py
    env/bin/python insert_test_data.py

At this point, the API is ready to run. However, you still need to build the client-side Ember app before running the server. 

### Client-side

Install the most recent versions of npm and node.js: 

    # Ubuntu
    apt-add-repository ppa:chris-lea/node.js
    apt-get update
    apt-get install nodejs
    # CentOS / RHEL
    yum install -y nodejs npm

Install ember-cli and bower:

    npm install -g ember-cli
    npm install -g bower

Change to `client` directory and install dependencies:

    cd client
    npm install
    bower install

Run the automatic builder (this will watch the folder for changes and re-build the client-side app if needed):

    ember build --watch

## Run

Once you have all dependencies installed, the client-side app built, and the database initialized, use one of the helper scripts to run the server (in the project's root directory): 

    env/bin/python run_dev.py

The server should now be serving a page at `http://localhost:5000/`. If you need to start the server in another way, simply read the run\_dev.py and run\_prod.py scripts, as they are fairly simple.

### Helper script

Running the script `dev_clean_restart.sh` will tear-down and re-initialize the database with placeholder values, then execute `run_dev.py`. This is for dev convenience only, and should **NEVER** be used on a production server, as it wipes the database. For this reason, the production instance has this script deleted. 

## Credits

### Client and Contacts

This project was developed for the Advanced Learning Technologies group at Miami University. The main client is Dr. Beth Rubin (rubinb at miamioh.edu). Our technical oversight was Dr. Greg Reese (reesegj at miamioh.edu). 

The authors are Michael Choate (choatemd at miamioh.edu or md.choate at gmail.com), Alex Dana (danaaj at miamioh.edu), and Blake Runkle (runklebc at miamioh.edu). Contact Michael Choate if *major* technical issues arise, or if insight is needed about the project's implementation. 

Small problems or requests (start/stop the service, etc.) should go to Amy Liu (liuz21 at miamioh.edu). 

### Components

Project structure based on [todo-flask-ember](https://github.com/gaganpreet/todo-flask-ember) by [Gaganpreet Singh Arora](https://github.com/gaganpreet).

Key components are [Flask](http://flask.pocoo.org/), [Flask-Restful](https://flask-restful.readthedocs.org/en/0.3.1/), [Flask-Restless](https://flask-restless.readthedocs.org/en/latest/), [SQLAlchemy](http://www.sqlalchemy.org/), [Ember.js](http://emberjs.com/), and [Twitter Bootstrap](http://getbootstrap.com/).
