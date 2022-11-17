from datetime import datetime
from app import db, bcrypt

exercisemusclegroup_table = db.Table(
    "exercisemusclegroup_table",
    db.Model.metadata,
    db.Column("exercise_id", db.ForeignKey("exercise.id")),
    db.Column("muscle_group_id", db.ForeignKey("muscle_group.id")),
)

class Exercise(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    
    machine_id = db.Column(db.Integer, db.ForeignKey("machine.id"))
    machine = db.relationship("Machine")
    
    name = db.Column(db.String, nullable=False)
    measure = db.Column(db.String, nullable=False)
    muscle_groups = db.relationship("MuscleGroup", secondary= exercisemusclegroup_table)
    how_to_use = db.Column(db.String, nullable=False)
    reps = db.Column(db.Integer, default=10)
    sets = db.Column(db.Integer, default=3)
    default_value = db.Column(db.String)