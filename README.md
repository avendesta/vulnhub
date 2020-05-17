# vulnhub
a vulnerable webapp, api setup script

- A flask web app
vulnerabilities

1 - easy to guess secret key
2 - jwt session similar for users of the same first name


# INITIAL SETUP
sudo apt install python3-pip
sudo apt install python3-virtualenv

#create project directory; 
#intialize virtualenvironment then activate it
mkdir flaskapp
virtualenv venv
source /venv/bin/activate
cd flaskapp
