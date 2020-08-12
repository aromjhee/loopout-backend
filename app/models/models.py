from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Session(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    duration = db.Column(db.String(8))

    def to_dictionary(self):
        return {
            'id': self.id,
            'name': self.name,
            'duration': self.duration
        }