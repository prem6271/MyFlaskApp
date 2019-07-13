import mysql.connector
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    # the column names should match with object properties.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    # cls means current Class
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethods
    # cls means current Class
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
