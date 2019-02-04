# SQLAlchemy_Flask_Ajax
Using Flask and SQLAlchemy for ETL of a sample dataset of Canadian cities and their population

#### How to convert a CSV file into a SQL database using SQLAlchemy
#### How to use the same database file in a web application using Flask and JavaScript Ajax

This sample project mainly consists of the following steps:
1. Reading a CSV file using the Python CSV module
2. Put records from CSV file into an SQLite database file using Python SQLAlchemy 
	* The first two steps are taken care of by **import.py** file
3. Build a Flask application that connects to and reads data from the same database 
4. Create JavaScript Ajax code to send requests to and receive responses from flask application

The requirements.txt includes all necessary modules plus _requests_ and _jupyter notebook_ libraries which we might make use of
in the next steps.
