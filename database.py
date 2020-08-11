from app.models.models import Session
from app import app, db
from dotenv import load_dotenv
load_dotenv()


with app.app_context():
    db.drop_all()
    db.create_all()

    session1 = Session(
        name='pomodoro',
        duration='0:25:0'
    )

    session2 = Session(
        name='break',
        duration='0:5:0'
    )

    db.session.add(session1)
    db.session.add(session2)
    db.session.commit()
