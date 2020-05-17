from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'iloveyou'
app.config['MONGO_DBNAME'] = "flaskapp"
app.config['MONGO_URI'] = "mongodb://localhost:27017/flaskapp"
app.config['WTF_CSRF_ENABLED'] = False

mongo = PyMongo(app)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/all" )
def getall():
    accounts = mongo.db.accounts
    all_user = []
    users = accounts.find()
    for u in users:
        u.pop('_id')
        all_user.append(u)
    return jsonify(all_user)

@app.route("/register", methods=['POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return "Registered successfully!!"
    else:
        return jsonify(form.errors)

@app.route("/login",methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return "Login sucessful"
    else:
        return jsonify(form.errors)

if __name__ == "__main__":
    app.run(debug=True)