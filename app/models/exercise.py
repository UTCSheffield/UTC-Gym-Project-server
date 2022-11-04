class Exercise(db.Model):
    id = db.Column(db.Integer, nullable=False)
    
    machine_id = Column(Integer, ForeignKey("Machine_table.id"))
    machine = relationship("Machine")
    
    name = sa.Column(db.String, nullable=False)
    machine = sa.Column(db.String, nullable=False)
    measure = sa.Column(db.String, nullable=False)
    muscle_groups = relationship("ExerciseMuscleGroup")
    how_to_use = db.Column(db.String, nullable=False)
