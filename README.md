# vulnhub
#### Vulnerable Flask-API script

###### _Vulnerabilities_

1. easy to guess secret key
1. jwt session similar for users of the same first name

###### SETUP ON UBUNTU
- cloning and virtualenv setup
```bash
git clone https/github.com/noodle-lover/vulnhub
cd vulnhub
virtualenv venv
source /venv/bin/activate 
# make sure its activated by running `which python` and `which pip`
cd flaskapp
```

- make sure to set environment variable before `flask run`
```bash
export FLASK_APP=blog.py 
# if you want debug mode `export FLASK_ENV=development`
pip install -r requirements.txt
flask run
```

- MongoDB Setup
  - install mongodb following the [official doc](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
  - install [mongodb compass](https://www.mongodb.com/download-center/compass)  ubuntu 
  - create database named `flaskapp` and table/collection named `accounts`
  - import the sample json data - `sample_db.json` into `accounts`
![flask-framework-wiki-image](https://bit.ly/2zP5qcU)
