from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from forms import RegistrationForm, LoginForm, RequestForm
from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity
from datetime import datetime, timedelta

app = Flask(__name__)

app.config['SECRET_KEY'] = 'iloveyou'
app.config['MONGO_DBNAME'] = "flaskapp"
app.config['MONGO_URI'] = "mongodb://localhost:27017/flaskapp"
app.config['WTF_CSRF_ENABLED'] = False
app.config['JWT_TOKEN_LOCATION'] = ['json']
app.config['JWT_SECRET_KEY'] = 'superSecret'

mongo = PyMongo(app)
jwt = JWTManager(app)


@app.route("/challenge",methods=["GET"])
def index():
    return jsonify({"goal-1":"log in as a previlaged user","goal-2":"find the secret_key of the webapp"})

@app.route("/all" )
def getall():
    accounts = mongo.db.accounts
    all_user = []
    users = accounts.find()
    for u in users:
        u.pop('_id')
        all_user.append(u)
    return jsonify(all_user)

@app.route("/get", methods=['GET'])
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
            return jsonify({"email":'email not found'})
    else:
        return jsonify(form.errors)

@app.route("/register", methods=['POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        accounts = mongo.db.accounts
        if accounts.find({"email":form.email.data}).count()>0:
            return jsonify(email="email already exist")
        else:
            accounts.insert_one({"username":username,"email":email,"password":password})
            return jsonify(username=username,email=email,password="****")
    else:
        return jsonify(form.errors)

@app.route("/login",methods=['POST'])
def login():
    form = LoginForm()
    accounts = mongo.db.accounts
    if form.validate_on_submit():
        email = form.email.data
        password = form.email.data
        fetch = accounts.find_one({"email":email})
        if fetch:
            username = fetch.get("username")
            expire = timedelta(minutes=1)
            access_token = create_access_token(identity=username,expires_delta=expire)
            return jsonify(access_token=access_token,email=email)
        else:
            return jsonify(result='Incorrect email or password')
    else:
        return jsonify(form.errors)

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/recover", methods=['GET'])
def recover():
    form = RequestForm(request.args)
    if form.validate():
        email = form.email.data
        element = mongo.db.accounts.find_one({'email':email})

        if element.get('username',None):
            username = element.get('username')
            email = element.get('email')
            return f"Dear {username}, this functionality is not implemented yet!"
        else:
            return jsonify({"email":'email not found'})
    else:
        return jsonify(form.errors)

@app.route("/help", methods=['GET'])
def admin():
    return "You can contact the admin via ricksanchez@adult.swim"
