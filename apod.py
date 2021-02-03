
# Please read the README.txt file

import urllib.request
import urllib.parse
import urllib.error
import datetime
import ssl
import json
import webbrowser
import sqlite3

# Ignore SSL Certificate Errors (I still don't understand anything in this. Just copied from Dr. Chuck's code3 folder)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Connecting Database and creating cursor object
database = sqlite3.connect("APOD.sqlite")
cursor = database.cursor()

# Date cannot be before 20/6/1995 or after Today

date = False
date = input("Enter date: ")
print()
# Validating Date here
if not date:
	date = datetime.datetime.today().strftime("%Y-%m-%d")
else:
	if "/" in date:
		try:
			date = datetime.datetime.strptime(date, "%d/%m/%y").strftime("%Y-%m-%d")
		except:
			date = datetime.datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")
	else:
		try:
			date = datetime.datetime.strptime(date, "%d-%m-%y").strftime("%Y-%m-%d")
		except:
			date = datetime.datetime.strptime(date, "%d-%m-%Y").strftime("%Y-%m-%d")

# Creating Table
cursor.executescript('''
CREATE TABLE IF NOT EXISTS APOD (
copyright TEXT,
date TEXT, 
explanation TEXT, 
hdurl TEXT, 
media_type TEXT,
service_version TEXT,
title TEXT, 
url TEXT, 
year INTEGER
)
''')

date = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%d-%m-%Y")
# Selecting Data from Database
cursor.execute('''
	SELECT copyright, date, explanation, hdurl, media_type, service_version, title, url, year FROM APOD WHERE date IS ( ? )
	''', (date, ))
from_sql = cursor.fetchone()
data_format = ("copyright", "date", "explanation", "hdurl", "media_type", "service_version", "title", "url", "year")

# Checking if already retrieved
if from_sql is not None:
	results = dict()
	for key, value in zip(data_format, from_sql):
		results[key] = value
	print("Collected data from cache")
	data = results
	del results
else:
	# Replace DEMO_KEY with your api key here. DEMO_KEY has some limitations. Read the README.txt file for more information. 
	api_key = "DEMO_KEY"
	if api_key == "DEMO_KEY":
		print("WARNING: If you use DEMO_KEY as the API key, Your limits are 30 requests per IP address per hour and 50 requests per IP address per day")
	date = datetime.datetime.strptime(date, "%d-%m-%Y").strftime("%Y-%m-%d")
	service_url = "https://api.nasa.gov/planetary/apod?"
	encoding_params = {"api_key": api_key}
	encoding_params['date'] = date
	encoding_params['thumbs'] = "True"
	# Retrieving the framed URL. If you don't understand the parameters, check the documentation of NASA API here : api.nasa.gov
	service_url += urllib.parse.urlencode(encoding_params)
	try:
		connection = urllib.request.urlopen(service_url, context=ctx)
	except Exception as error:
		print(f"Error: {error}")
		print(f"Request URL: {service_url}")
		quit()

	results = connection.read().decode()
	headers = dict(connection.getheaders())
	print("Number of Requests Remaining for Today: ", headers["X-RateLimit-Remaining"])
	data = json.loads(results)
	data['date'] = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%d-%m-%Y")
	data['year'] = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%Y")
	if not 'copyright' in data:
		data['copyright'] = "National Aeronautics and Space Administration (NASA)"
	# Writing the retrieved data from API to Database so that we don't have to retrieve it again. 
	cursor.execute('''
		INSERT INTO APOD (copyright, date, explanation, hdurl, media_type, service_version, title, url, year) VALUES 
		(?, ?, ?, ?, ?, ?, ?, ?, ?) ''', 
		(data['copyright'], data['date'], data['explanation'], data['hdurl'], data['media_type'], data['service_version'], data['title'], data['url'], data['year']))
	database.commit()

# Here, we're writing our retrieved data to a JavaScript file called variables.js
# The app.js is going to retrieve the data from variables.js and put it into the index.html file. 
# Just think the variables.js as the connection between our Python script and the JavaScript of HTML
# Actually I didn't know any JavaScript. I just cruised through the web to learn something when writing this project. 
variables = open("variables.js", "w")
var_data = "var vars = \n"
var_data += str(data)
var_data += ";"
variables.write(var_data)
webbrowser.open("index.html")