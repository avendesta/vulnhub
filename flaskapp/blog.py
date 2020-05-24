from flask import Flask, request, jsonify, send_from_directory, redirect, url_for
from flask_pymongo import PyMongo
from forms import RegistrationForm, LoginForm, RequestForm
from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity
from datetime import datetime, timedelta

app = Flask(__name__,static_folder='static')

app.config['MONGO_DBNAME'] = "flaskapp"
app.config['MONGO_URI'] = "mongodb://localhost:27017/flaskapp"
app.config['WTF_CSRF_ENABLED'] = False
app.config['JWT_TOKEN_LOCATION'] = ['json']
app.config['JWT_SECRET_KEY'] = 'qwerty123456'

mongo = PyMongo(app)
jwt = JWTManager(app)

@app.route("/")
def index():
    return jsonify(status='up')

@app.route("/api/challenge")
def base():
    return jsonify({"goal-1":"log in as a previleged/admin user",
    "goal-2":"find the secret_key of this flask webapp",
    "note":"please do not brute force the site, it won't help"
    })


@app.route("/api/get", methods=['GET'])
@jwt_required
def get():
    form = RequestForm(request.args)
    if form.validate():
        email = form.email.data
        current_user = get_jwt_identity()
        element = mongo.db.accounts.find_one({'email':email})

        if element and current_user == element.get('username'):
            username = element.get('username')
            email = element.get('email')
            return jsonify(username=username,email=email)
        else:
            return jsonify({"email":'email not found'}),400
    else:
        return jsonify(form.errors),400

@app.route("/api/register", methods=['POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        accounts = mongo.db.accounts
        if accounts.find({"email":form.email.data}).count()>0:
            return jsonify(email="email already exist"),400
        else:
            accounts.insert_one({"username":username,"email":email,"password":password})
            return jsonify(username=username,email=email,password="****"), 201
    else:
        return jsonify(form.errors), 400

@app.route("/api/login",methods=['POST'])
def login():
    form = LoginForm()
    accounts = mongo.db.accounts
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        fetch = accounts.find_one({"email":email,"password":password})
        if fetch:
            username = fetch.get("username")
            expire = timedelta(minutes=30)
            access_token = create_access_token(identity=username,expires_delta=expire)
            return jsonify(access_token=access_token,email=email)
        else:
            return jsonify(msg='Incorrect email or password'),400
    else:
        return jsonify(form.errors),400

@app.route("/api/recover", methods=['GET'])
def recover():
    form = RequestForm(request.args)
    if form.validate():
        email = form.email.data
        element = mongo.db.accounts.find_one({'email':email})

        if element:
            username = element.get('username')
            email = element.get('email')
            return f"Dear {username}, this functionality is not implemented yet!", 202
        else:
            return jsonify({"email":'email not found'}),400
    else:
        return jsonify(form.errors),404

@app.route("/api/help", methods=['GET'])
def help():
    return jsonify(msg="You can contact the admin via peradiso@fake.flask")

@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == "__main__":
    app.run(debug=True)
