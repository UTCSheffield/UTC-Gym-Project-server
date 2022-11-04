class Session(db.Model):
    id = db.Column(db.Integer,nullable=False)
    
    user_id = Column(Integer, ForeignKey("user.id"))
    
    exercies = relationship("SessionExercise")
    
    User = sa.Column(db.String, nullable=False)
    location = sa.Column(db.String, nullable=False)
    startDateTime = sa.Column(db.DateTime, nullable=False)
    endTime = sa.Column(db.DateTime, nullable=False)
