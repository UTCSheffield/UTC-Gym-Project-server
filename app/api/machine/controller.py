from flask_restx import Resource
from flask_jwt_extended import jwt_required

from .service import MachineService
from .dto import MachineDto

api = MachineDto.api
data_resp = MachineDto.data_resp


@api.route("/<string:machinename>")
class MachineGet(Resource):
    @api.doc(
        "Get a specific machine",
        responses={
            200: ("Machine data successfully sent", data_resp),
            404: "Machine not found!",
        },
    )
    @jwt_required()
    def get(self, machinename):
        """ Get a specific machine's data by their machinename """
        return MachineService.get_machine_data(machinename)
