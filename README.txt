Contents of the Repository :
	--> apod.py
	--> app.js
	--> index.html
	--> styles.css
	--> variables.js

Explanation of each file :
1) apod.py
	-> Imports urllib for retrieving the API's URL
	-> Imports datetime for date-related things
	-> Imports ssl for ignoring SSL Certificate Errors
	-> Imports json for parsing the retrieved content
	-> Imports sqlite3 for sql related things
	-> Imports webbrowser for opening the html file in the browser
	-> Creates connection to APOD.sqlite file, creates cursor object of sqlite3 library
	-> There are two ways of running the program. One is without the input statement for date. If it is commented out, the date is going to be today's date.
	-> If the input line is not commented out, gets date from user as input and validates it with conditions and datetime module
	-> When we frame the URL, date is the most important parameter to carefully look after. Because, we get the data according to the date.
	-> The date has to be in yyyy-mm-dd format. So, we have to make sure that, We convert the input date to this format with the datetime module.
	-> Creates Table in APOD.sqlite with all needed rows
	-> Selects data in APOD.sqlite if they are there (You will understand why soon)
	-> Go to this URL and see an example to understand the format of how the API returns data : https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY
	-> Checks if the data returned from the SELECT sqlite statement is None. If not None, it prepares the data from it.
	-> If the data returned from the SELECT sqlite statement is None, frames an URL and talks to the NASA APOD API for the data. 
	-> Retrieves the data and decodes it, gets the headers for seeing the number of requests remaining. 
	-> The retrieved data contains 'copyright' key rarely. So, If copyright is not there, assumes NASA as the copyright holder.
	-> Writes the retrieved data to the APOD.sqlite file. This way, we don't have to retrieve already retrieved date's data again. 
	-> Commits the changes to the APOD.sqlite file.
	-> Writes the either way retrieved data to variables.js file.
	-> Opening index.html.
	-> In index.html, both app.js and variables.js are linked with a script tag. So, app.js can get the data from variables.js. 
	-> Then, app.js is going to fill all the placeholders in index.html. The placeholders are going to be the retrieved data only.

2) app.js
	-> Selects the placeholders in index.html and replaces them with the data in variables.js file. 

3) index.html
	-> Has the skeleton of the project. Contains the default things like the main header and title and has lot of placeholders which will be filled by app.js

4) styles.css
	-> Styles the index.html. Just try moving the styles.css file to somewhere other than the same directory as index.html and see what happens to index.html. 