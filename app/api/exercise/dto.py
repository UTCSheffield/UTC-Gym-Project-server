from flask_restx import Namespace, fields


class ExerciseDto:

    api = Namespace("exercise", description="Exercise related operations.")
    exercise = api.model(
        "Exercise object",
        {
            "name": fields.String
            "measure": fields.String
            "muscle_groups": fields.String
            "how_to_use": Fields.String
            "reps": fields.Integer
            "sets": fields.Integer
            "default_value": fields.Integer

        },
    )

    data_resp = api.model(
        "Exercise Data Response",
        {
            "exercise": fields.Nested(exercise),
        },
    )
