# Model Schemas
from app import ma
from .user import User


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("email", "name", "username", "joined_date", "role_id")


from .session import Session

class SessionSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("User", "location", "startDateTime", "endTime", "role_id")


from .exercise import Exercise

class ExerciseSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("name", "machine", "measure", "how_to_use", "role_id")


from .sessionExercise import SessionExercise

class SessionExerciseSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("start", "end", "reps", "value", "role_id")


from .measurement import Measurement

class MeasurementSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("date", "height", "resting", "role_id")


from .machine import Machine

class MachineSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("name", "role_id")