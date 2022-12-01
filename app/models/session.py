from datetime import datetime
from app import db, bcrypt

class Session(db.Model):
    id = db.Column(db.Integer,nullable=False, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    #user = db.relationship("User")

    exercises = db.relationship("SessionExercise")
    total_calories = db.Column(db.Integer)
    location = db.Column(db.String, nullable=False)
    startDateTime = db.Column(db.DateTime, nullable=False)
    endTime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return str(self.id) + "-" + str(self.startDateTime)

    def get_total_calories(self):
        self.total_calories = 0
        for exercise in self.exercises:
            self.total_calories += exercise.calories