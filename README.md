# vulnhub
a vulnerable webapp, api setup script

- A flask web app
vulnerabilities

1 - easy to guess secret key
2 - jwt session similar for users of the same first name


# INITIAL SETUP
sudo apt install python3-pip
sudo apt install python3-virtualenv
#make sure pwd = vulnhub/
virtualenv venv 
# or
# pip3 install virtualenv; python3 -m virtualenv venv

#activate virtualenv
source /venv/bin/activate
cd flaskapp

# make sure to set environment variable before `flask run`
export FLASK_APP=blog.py
pip install -r requirements.txt
flask run
