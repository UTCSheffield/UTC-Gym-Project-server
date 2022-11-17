from flask_restx import Namespace, fields


class MachineDto:

    api = Namespace("machine", description="Machine related operations.")
    machine = api.model(
        "Machine object",
        {
            "name": fields.String
        },
    )

    data_resp = api.model(
        "Machine Data Response",
        {
            "machine": fields.Nested(machine),
        },
    )
