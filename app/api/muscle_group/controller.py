from flask_restx import Resource
from flask_jwt_extended import jwt_required

from .service import Muscle_groupService
from .dto import Muscle_groupDto

api = Muscle_groupDto.api
data_resp = Muscle_groupDto.data_resp


@api.route("/<string:muscle_groupname>")
class Muscle_groupGet(Resource):
    @api.doc(
        "Get a specific muscle_group",
        responses={
            200: ("Muscle_group data successfully sent", data_resp),
            404: "Muscle_group not found!",
        },
    )
    @jwt_required()
    def get(self, muscle_groupname):
        """ Get a specific muscle_group's data by their muscle_groupname """
        return Muscle_groupService.get_muscle_group_data(muscle_groupname)
