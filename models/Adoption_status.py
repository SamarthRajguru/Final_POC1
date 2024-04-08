
from create_app import db

class AdoptionStatus(db.Model):
    __tablename__ = 'adoption_status'

    status_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)

print("AdoptionStatus table created")

