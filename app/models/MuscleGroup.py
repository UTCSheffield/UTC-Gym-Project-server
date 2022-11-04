class MuscleGroup(db.Model):
    id = db.Column(db.Integer, nullable=False)
    
    exercise_id = Column(Integer, ForeignKey("exercise.id"))
    exercise = relationship("Exercise")
    
    name = sa.Column(db.String, nullable=False)
