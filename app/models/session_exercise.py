from app import db, bcrypt
from datetime import timedelta

class SessionExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
   
    session_id = db.Column(db.ForeignKey("session.id"))
    session = db.relationship("Session", back_populates="exercises")
    exercise_id = db.Column(db.ForeignKey("exercise.id"))
    exercise = db.relationship("Exercise")

    start = db.Column(db.DateTime, nullable=False, default=db.func.now())
    end = db.Column(db.DateTime, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    perc_diff = db.Column(db.Integer, nullable=False, default=3)
    notes = db.Column(db.String)
    units = db.Column(db.String, nullable=False)
    calories = db.Column(db.Integer)
    value = db.Column(db.Integer, nullable=False)

    def suggestion(self):
        # weights
        if self.exercise.suggestion_type == "weights":
            print("Is a weight")
        '''
        but based on the BORG numbers
        MATHS FOR CHANGING HOW MUCH THE WEIGHT INCREASES BY:
Idea 1:
	Ask them after the exercise how easy they found the exercise, on a scale of 1 to 5. 1 = Barely Doable
											    2 = Doable for short periods of time
											    3 = Doable fairly easily 
										 	    4 = Easy
											    5 = Very Easy
	After a certain amount of times of answering 4/5, suggest a higher weight than the current one. 
	If 3 is answered, tell user to keep on doing what they are doing.
	After a certain amount of times of answering 1/2, suggest a lower weight than the current one.
	If the user misses gym days consecutively, it will let them know that their reccomended weight class is lowered.


ANY additional ideas will be added here. Please suggest any.
round to sensible kg numbers
        '''

        # ONE REP MAX
        if self.exercise.suggestion_type == "onerep":
            print("Is a weight")


        if self.exercise.suggestion_type == "cardio":
            print("SAME AS WEIGHT BUT DOESN'T ROUND")

        

        else:
            self.reps = self.exercise.default_reps
            self.sets = self.exercise.default_sets
            self.value = self.exercise.default_value

    def calc_calories(self):
        MET = (self.exercise.vigorous_met/8) * self.perc_diff
        duration = (self.end-self.start) / timedelta(minutes=1)
        weight = int(self.session.user.measurements[-1].weight)
        self.calories = (duration)*(MET*3.5*weight)/200
