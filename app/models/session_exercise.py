from app import db, bcrypt
from datetime import timedelta

class SessionExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
   
    session_id = db.Column(db.ForeignKey("session.id"))
    session = db.relationship("Session", back_populates="exercises")
    exercise_id = db.Column(db.ForeignKey("exercise.id"))
    exercise = db.relationship("Exercise")#, back_populates="sessions")

    start = db.Column(db.DateTime, nullable=False, default=db.func.now())
    end = db.Column(db.DateTime, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    perc_diff = db.Column(db.Integer, nullable=False, default=3)
    notes = db.Column(db.String)
    units = db.Column(db.String, nullable=False)
    calories = db.Column(db.Integer)
    suggestion_type = db.Column(db.String, nullable=False)

    def suggestion(self):
        if self.suggestion_type == "weights":
            print("Is a weight")
        if self.exercise:
            self.reps = self.exercise.default_reps
            self.sets = self.exercise.default_sets
            self.value = self.exercise.default_value

    def calc_calories(self):
        MET = (self.exercise.vigorous_met/8) * self.perc_diff
        duration = (self.end-self.start) / timedelta(minutes=1)
        weight = int(self.session.user.measurements[-1].weight)
        self.calories = (duration)*(MET*3.5*weight)/200 # calculate calories here

