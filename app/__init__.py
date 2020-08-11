from flask import Flask, request, jsonify
from app.config import Configuration
from app.models.models import db, Session
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "supports_credentials": True}})
app.config.from_object(Configuration)
db.init_app(app)
Migrate(app, db)
# pipenv run flask db init
# pipenv run flask db migrate -m 'first migration'
# pipenv run flask db upgrade


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