## Miami University e-Learning Course Database

Repository for Miami University's online course database, for use by the
Advanced Learning Technologies group. 

* Backend API written in Python using Flask-Restful (/api directory)
* Frontend written in Javascript using Ember.js (/client directory)

Project structure based on [todo-flask-ember](https://github.com/gaganpreet/todo-flask-ember) by [Gaganpreet Arora](https://github.com/gaganpreet).

## Setup

(Assuming Ubuntu 12.x with Python installed)

Clone the repo: 

    https://github.com/mdchoate/MU-e-Learning-Database.git
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

## Run

Run init\_db.py to initialize the database tables. init\_test\_data.py will
insert some placeholder data into the database. There are two helper scripts, 
run\_dev.py and run\_prod.py, to start the server.
