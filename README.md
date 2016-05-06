About this APP:
It provides an API to register logs/messages, there is a dashboard which present the server info continuously.

Features:
1)Server accepts logs/messages from a client and stores them at a central location.
2)Dashboard which provides the below details:
  CPU details of the system every second for a duration of 5 minutes.
  Message Logging hits to the system every second for a duration of 60  seconds.
	CPU details includes CPU usage percent,physical memory usage,io read ,io write..

 List all the logs in the system .

3) Implemented logviewer which is similar to 'tail -f' displays the logs in the server.


Dependencies:
1) requires 'psutil' for getting cpu statistics.
 in order to install , do 'pip install psutil'

 this psutil might require few more dependencies , install them


How to use this APP:
1) unzip do 'python manage.py makemigrations Dashboard' then 'python manage.py makemigrations LogAggregatorService' then 'python manage.py makemigrations LogViewer' 'python manage.py makemigrations MessageLogger' then 'python manage.py migrate'
for creating the schemas
2) run the server using 'python manage.py runserver'
3) In order to log the message, client should be registered, which can be done by putting the data into the ClientTokens.
4) Create superuser account using 'python manage.py createsuperuser' which prompts for username and password.
5) login to admin (<url>/admin/) console and add the token and email_id's
6) in order to put data into the logs four parameters to be passed to the <url>/log/ url using POST method: they are - client_token,log_name,log_level,message
7)in order to open the dashboard <url>/dashboard/ which the dashboard.
 below there is log list , create on the last column to open the log in the web log viewer.

Resources:
1) googlecharts javascript to display the graphs
2) JQuery/AJAX
3) Bootstrap for frontend