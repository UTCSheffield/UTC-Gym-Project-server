# Model Schemas
from app import ma
from .user import User


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("email", "name", "username", "joined_date")


from .session import Session

class SessionSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("User", "location", "startDateTime", "endTime")


from .exercise import Exercise

class ExerciseSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("name", "machinename", "measure", "how_to_use", "default_reps", "default_sets", "exercise_type")


from .session_exercise import SessionExercise

class SessionExerciseSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("start", "end", "reps", "value")


from .measurement import Measurement

class MeasurementSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("date", "height", "resting")


from .machine import Machine

class MachineSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ["name"]


from .muscle_group import MuscleGroup

class Muscle_groupSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ["name"]