from datetime import datetime
from app import db, bcrypt

class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    #user = db.relationship("User")
    date = db.Column(db.DateTime, nullable=False) # we don't know what all  the datatypes are
    height = db.Column(db.Integer, nullable=False)
    resting_heartrate = db.Column(db.Integer)
    weight = db.Column(db.Integer, nullable=False)
    bmi = db.Column(db.Float)
    sex = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    body_fat = db.Column(db.Integer) #0 is male 1 is female

    def calc_bmi(self):
        self.bmi = round((self.weight / (self.height**2)) * 10000, 1)

    def calc_body_fat(self):
        print(self.age, self.sex, self.bmi)
        self.body_fat = -44.988 + (0.503 * self.age) + (10.689*self.sex) + (3.172*self.bmi) - (0.026*(self.bmi**2)) + (0.181*self.bmi*self.sex) - (0.02*self.bmi*self.age) - (0.005 * (self.bmi**2) * self.sex) + (0.00021*(self.bmi**2) * self.age)