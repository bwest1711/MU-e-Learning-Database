#!/bin/bash

# This script patches a core component of flask-restful to make it work with 
# Ember.js without breaking everything. This is a BAD IDEA, and if the file 
# that it modifies is updated or changed in any way, it will break. Until the
# flask extension is updated, this script NEEDS to be run after every install,
# after `pip install -r requirements.txt` is run.

# Summary of the problem: https://github.com/jfinkels/flask-restless/issues/403

sed -i "363i \ \ \ \ \ \ \ \ result[relation] = [v.id for v in relatedvalue]" env/lib/python2.7/site-packages/flask_restless/helpers.py
sed -i "364i \ \ \ \ \ \ \ \ continue" env/lib/python2.7/site-packages/flask_restless/helpers.py
