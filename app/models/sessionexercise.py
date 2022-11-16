from datetime import datetime
from app import db, bcrypt

class SessionExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
   
    session_id = db.Column(db.ForeignKey("session.id"))
    #session = db.relationship("Session")
    exercise_id = db.Column(db.ForeignKey("exercise.id"))
    exercise = db.relationship("Exercise")

    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float, nullable=False)
    perc_diff = db.Column(db.Integer, nullable=False, default=3)
    notes = db.Column(db.String)

    def suggestion(self):
        pass