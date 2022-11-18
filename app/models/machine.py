from datetime import datetime
from app import db, bcrypt

class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    #exercises = db.relationship("Exercise")
    
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.name