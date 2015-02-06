#!/bin/bash
set -e

echo 'Setting up database.'
env/bin/python init_db.py
echo 'Inserting test data.'
env/bin/python insert_test_data.py
echo 'Starting server.'
env/bin/python run_dev.py
