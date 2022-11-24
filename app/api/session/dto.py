from flask_restx import Namespace, fields


class SessionDto:

    api = Namespace("session", description="Session related operations.")
    session = api.model(
        "Session object",
        {
            "email": fields.String,
            "name": fields.String,
            "sessionname": fields.String,
            "joined_date": fields.DateTime,
            "role_id": fields.Integer,
        },
    )

    data_resp = api.model(
        "Session Data Response",
        {
            "status": fields.Boolean,
            "message": fields.String,
            "session": fields.Nested(session),
        },
    )
