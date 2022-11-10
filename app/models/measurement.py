from datetime import datetime
from app import db, bcrypt

class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    #user = db.relationship("User")
    date = db.Column(db.DateTime, nullable=False) # we don't know what all  the datatypes are
    height = db.Column(db.Integer, nullable=False)
    resting_heartrate = db.Column(db.Integer, nullable=False)
