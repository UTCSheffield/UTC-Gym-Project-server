from datetime import datetime
from app import db, bcrypt

class MuscleGroup(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercise.id"))
    exercise = db.relationship("Exercise")
    
    name = db.Column(db.String, nullable=False)
