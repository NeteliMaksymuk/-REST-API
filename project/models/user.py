from project.db import db


class UserModel(db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128))
    record = db.relationship('RecordModel', back_populates="user", lazy='dynamic')


