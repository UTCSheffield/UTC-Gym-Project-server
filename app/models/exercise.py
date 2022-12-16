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
    
    name = db.Column(db.String, nullable=False, unique=True)
    units = db.Column(db.String, nullable=False, default="kg")
    muscle_groups = db.relationship("MuscleGroup", secondary=exercisemusclegroup_table)
    how_to_use = db.Column(db.String)
    default_reps = db.Column(db.Integer, default=10)
    default_sets = db.Column(db.Integer, default=3)
    default_value = db.Column(db.Float)
    default_perc_def = db.Column(db.Integer, default=3)
    vigorous_met = db.Column(db.Float, nullable=False, default=5.5)

    def __repr__(self):
        return self.name