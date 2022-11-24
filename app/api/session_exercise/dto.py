from flask_restx import Namespace, fields


class Session_exerciseDto:

    api = Namespace("session_exercise", description="Session_exercise related operations.")
    session_exercise = api.model(
        "Session_exercise object",
        {
            "email": fields.String,
            "name": fields.String,
            "session_exercisename": fields.String,
            "joined_date": fields.DateTime,
            "role_id": fields.Integer,
        },
    )

    data_resp = api.model(
        "Session_exercise Data Response",
        {
            "status": fields.Boolean,
            "message": fields.String,
            "session_exercise": fields.Nested(session_exercise),
        },
    )
