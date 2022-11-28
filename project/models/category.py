from project.db import db


class CategoryModel(db.Model):
    __tablename__ = "Category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey("User.id"))
    record = db.relationship('RecordModel', back_populates="category", lazy='dynamic')

