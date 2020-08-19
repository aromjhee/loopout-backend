from app.models.models import Session
from app import app, db
from dotenv import load_dotenv
load_dotenv()


with app.app_context():
    db.drop_all()
    db.create_all()

    s1 = Session(
        name='cool down time',
        duration='0:5:0'
    )

    s2 = Session(
        name='head to bathroom',
        duration='0:0:30'
    )

    s3 = Session(
        name='wash up',
        duration='0:0:30'
    )

    s4 = Session(
        name='brush teeth',
        duration='0:2:0'
    )

    s5 = Session(
        name='make breakfast',
        duration='0:5:0'
    )

    s6 = Session(
        name='eat',
        duration='0:5:0'
    )

    s7 = Session(
        name='relax',
        duration='0:5:0'
    )

    s8 = Session(
        name='put on shoes',
        duration='0:0:45'
    )

    s9 = Session(
        name='headout to subway station',
        duration='0:10:0'
    )

    db.session.add_all([s1, s2, s3, s4, s5, s6, s7, s8, s9])
    db.session.commit()
