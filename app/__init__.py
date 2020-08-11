from flask import Flask
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