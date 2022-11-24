from flask_restx import Namespace, fields


class Muscle_groupDto:

    api = Namespace("muscle_group", description="Muscle_group related operations.")
    muscle_group = api.model(
        "Muscle_group object",
        {
            "email": fields.String,
            "name": fields.String,
            "muscle_groupname": fields.String,
            "joined_date": fields.DateTime,
            "role_id": fields.Integer,
        },
    )

    data_resp = api.model(
        "Muscle_group Data Response",
        {
            "status": fields.Boolean,
            "message": fields.String,
            "muscle_group": fields.Nested(muscle_group),
        },
    )
