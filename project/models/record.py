from sqlalchemy import func

from project.db import db


class RecordModel(db.Model):
    __tablename__ = "Record"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"), unique=False, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("Category.id"), unique=False, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=func.now())
    sum = db.Column(db.Float(precision=2), unique=False, nullable=False)

    user = db.relationship('UserModel', back_populates="record")
    category = db.relationship('CategoryModel', back_populates="record")

