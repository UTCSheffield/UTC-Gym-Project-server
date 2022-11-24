from flask_restx import Namespace, fields


class MeasurementDto:

    api = Namespace("measurement", description="Measurement related operations.")
    measurement = api.model(
        "Measurement object",
        {
            "email": fields.String,
            "name": fields.String,
            "measurementname": fields.String,
            "joined_date": fields.DateTime,
            "role_id": fields.Integer,
        },
    )

    data_resp = api.model(
        "Measurement Data Response",
        {
            "status": fields.Boolean,
            "message": fields.String,
            "measurement": fields.Nested(measurement),
        },
    )
