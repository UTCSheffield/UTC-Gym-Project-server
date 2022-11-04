class SessionExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
   
    session_id = Column(ForeignKey("session.id"))
    session = relationship("Session")
    exercise_id = Column(ForeignKey("exercise.id"))
    exercise = relationship("Exercise")

    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float, nullable=False)
