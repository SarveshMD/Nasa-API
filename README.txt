Contents of the Repository :
	--> apod.py
	--> reset.py
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

2) reset.py
	-> Imports os for deleting APOD.sqlite
	-> Deletes APOD.sqlite
	-> Opens variables.js and truncates it

3) app.js
	-> Selects the placeholders in index.html and replaces them with the data in variables.js file. 

4) index.html
	-> Has the skeleton of the project. Contains the default things like the main header and title and has lot of placeholders which will be filled by app.js

5) styles.css
	-> Styles the index.html. Just try moving the styles.css file to somewhere other than the same directory as index.html and see what happens to index.html. 

Finally, Here's the part which explains the Limitations of using DEMO_KEY as the API KEY for retrieving data from NASA API. 
First, let me give you a summary of what's coming next. 

With DEMO_KEY as the API Key, you are limited to, 
	-> 30 Requests per IP address per hour, That is, probably 30 requests per hour with a device.
	-> 50 Requests per IP address per day, That is, probably 50 requests per day with a device.

But with your API Key, you are limited to, 
	-> 1000 requests per hour. That is 24,000 requests per day.

If you are wondering of how to get an API key, It's a two click job.
	-> Head to https://api.nasa.gov/
	-> Scroll down a bit until you see the Generate API Key heading.
	-> Go ahead and give your Name and Email Address and hit the signup button.
	-> You should see your API Key in the page once you hit the signup button and that's it. 

############################     This is the original notes on Request Limits copied from NASA's https://api.nasa.gov website.     ############################

Web Service Rate Limits
Limits are placed on the number of API requests you may make using your API key. Rate limits may vary by service, but the defaults are:

Hourly Limit: 1,000 requests per hour
For each API key, these limits are applied across all api.nasa.gov API requests. Exceeding these limits will lead to your API key being temporarily blocked from making further requests. The block will automatically be lifted by waiting an hour. If you need higher rate limits, contact us.

DEMO_KEY Rate Limits
In documentation examples, the special DEMO_KEY api key is used. This API key can be used for initially exploring APIs prior to signing up, but it has much lower rate limits, so you’re encouraged to signup for your own API key if you plan to use the API (signup is quick and easy). The rate limits for the DEMO_KEY are:

Hourly Limit: 30 requests per IP address per hour
Daily Limit: 50 requests per IP address per day
How Do I See My Current Usage?
Your can check your current rate limit and usage details by inspecting the X-RateLimit-Limit and X-RateLimit-Remaining HTTP headers that are returned on every API response. For example, if an API has the default hourly limit of 1,000 request, after making 2 requests, you will receive this HTTP header in the response of the second request:

X-RateLimit-Remaining: 998

The hourly counters for your API key reset on a rolling basis.

Example: If you made 500 requests at 10:15AM and 500 requests at 10:25AM, your API key would become temporarily blocked. This temporary block of your API key would cease at 11:15AM, at which point you could make 500 requests. At 11:25AM, you could then make another 500 requests.

Anyone can register for an api.nasa.gov key, which can be used to access data across federal agencies.

############################                                End of notes copied from NASA's website                                ############################

								Have fun with the NASA API !!!

