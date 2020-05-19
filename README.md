# vulnhub
a vulnerable webapp, api setup script

- A flask web app
vulnerabilities

1 - easy to guess secret key
2 - jwt session similar for users of the same first name


**INITIAL SETUP**
*git clone https/github.com/noodle-lover/vulnhub*

*cd vulnhub*

*virtualenv venv *

**activate virtualenv**
*source /venv/bin/activate*

*cd flaskapp*

**make sure to set environment variable before `flask run`**
*export FLASK_APP=blog.py*
*pip install -r requirements.txt*
*flask run*


**MONGODB SETUP**
1- install mongodb following the official doc
"https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/"
2- install mongodb compass following
"https://www.mongodb.com/download-center/compass"
3- create mongo app named 'flaskapp' and document named 'accounts'
4- import sample json data - sample_db.json into it
