from datetime import datetime

from .. import db


class Company(db.Model):
    __tablename__ = "company"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    website = db.Column(db.String, nullable=True)
    type = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    country = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=True)
    postal_code = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    telephone_number = db.Column(db.String, nullable=True)
    google_score = db.Column(db.String, nullable=True)
    google_review_count = db.Column(db.String, nullable=True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime)


    @property
    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'address': self.address,
            'telephone number': self.telephone_number,
            'google score': self.google_score,
            'created date': self.created_date,
        }