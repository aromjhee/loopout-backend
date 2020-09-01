from flask import Flask, request, jsonify
from app.config import Configuration
from app.models.models import db, Session, User
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import bcrypt


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "supports_credentials": True}})
app.config.from_object(Configuration)
db.init_app(app)
Migrate(app, db)
# pipenv run flask db init
# pipenv run flask db migrate -m 'first migration'
# pipenv run flask db upgrade
jwt = JWTManager(app)


@app.route('/')
def index():
    """ get all session """
    sessions = Session.query.all()
    data = [session.to_dictionary() for session in sessions]
    return {'sessions': data}


@app.route('/add', methods=['POST'])
def add():
    """ add a new session """
    new_session = Session(**request.json)
    db.session.add(new_session)
    db.session.commit()
    return {'sessions': new_session.to_dictionary()}


@app.route('/<int:id>/delete', methods=['DELETE'])
def delete(id):
    """ delete session """
    session_to_delete = Session.query.get(int(id))

    if session_to_delete:
        db.session.delete(session_to_delete)
        db.session.commit()
        return {'message': 'Session deleted.'}
    else:
        return {'message': 'Session not found'}


@app.route('/register', methods=['POST'])
def register():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        repassword = request.json.get('repassword')

        if not email:
            return jsonify(message='Missing email address'), 400
        if not password:
            return jsonify(message='Missing password'), 400
        if not repassword or password != repassword:
            return jsonify(message='Please re-enter password'), 400

        check_if_email_exists = User.query.filter_by(email=email).first()
        if check_if_email_exists:
            return jsonify(message='The email already exists'), 400
        
        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt()
        ).decode('utf-8')
        
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        access_token = create_access_token(identity={'email': email})
        return jsonify(message='New User Created', email=email, access_token=access_token), 200
    except:
        return jsonify(message='Error when registering'), 400


@app.route('/login', methods=['POST'])
def login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')

        if not email:
            return jsonify(message='Missing email address'), 400
        if not password:
            return jsonify(message='Missing password'), 400

        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify(message='User Not Found'), 400
        print(user.email)
        if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            access_token = create_access_token(identity={'email': email})
            return jsonify(access_token=access_token), 200
        else:
            return jsonify(message='Invalid Email and Password'), 400
    except Exception as e:
        return jsonify(message='Error when logging in user'), 400
        # return print(e)
