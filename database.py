from app.models.models import Session, User
from app import app, db
from dotenv import load_dotenv
load_dotenv()
import bcrypt


with app.app_context():
    db.drop_all()
    db.create_all()

    password = 'asdf'

    hashed_password = bcrypt.hashpw(
        password.encode('utf-8'), bcrypt.gensalt()
    ).decode('utf-8')

    test_user = User(email='test@test.com', password=hashed_password)

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

    s1.user = test_user
    s2.user = test_user
    s3.user = test_user
    s4.user = test_user
    s5.user = test_user
    s6.user = test_user
    s7.user = test_user
    s8.user = test_user
    s9.user = test_user

    db.session.add(test_user)
    db.session.add_all([s1, s2, s3, s4, s5, s6, s7, s8, s9])
    db.session.commit()
