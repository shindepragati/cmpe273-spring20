
# Aassignment 2:

# .py files
1. createtable.py - execute first so it creates two table 'pratests' and 'prasubmissions' in sqlite db

2.db.py - contains all queries related sqlite db- create table, insert data, querytable etc

3.allapi.py - contains api devloped to store actual test data to db, fetch stored scantron submission and actual tests data,  download file, upload file

4.apiController.py - is a helper class for allapi.py, contains all methods get data from db, process and send to allapi.py

# Curl command:

curl -F 'data=@scantron-1.json' http://127.0.0.1:5000/api/tests/1/scantrons

http://127.0.0.1:5000 - localhost , please change according to ur localhost address
