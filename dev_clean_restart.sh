#!/bin/bash
set -e

# NOTE: For development convenience only. This should be removed from the
# production server IMMEDIATELY to avoid accidents. 
echo 'Removing old database.'
rm -f app.db
echo 'Setting up new database.'
python init_db.py
echo 'Inserting test data.'
python insert_test_data.py
echo 'Starting server.'
python run_dev.py
