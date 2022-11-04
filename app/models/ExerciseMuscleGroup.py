class ExerciseMuscleGroup(Base):
  exercise_id = Column(ForeignKey("exercise.id"), primary_key = True)
  muscle_group_id = Column(ForeignKey("muscle_group.id"), primary_key = True)
  exercise = relationship("Exercise")
#  muscle_group = relationship("MuscleGroup")
