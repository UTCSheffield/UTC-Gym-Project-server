from flask_restx import Resource
from flask_jwt_extended import jwt_required

from .service import Session_exerciseService
from .dto import Session_exerciseDto

api = Session_exerciseDto.api
data_resp = Session_exerciseDto.data_resp


@api.route("/<string:session_exercisename>")
class Session_exerciseGet(Resource):
    @api.doc(
        "Get a specific session_exercise",
        responses={
            200: ("Session_exercise data successfully sent", data_resp),
            404: "Session_exercise not found!",
        },
    )
    #@jwt_required()
    def get(self, session_exercisename):
        """ Get a specific session_exercise's data by their session_exercisename """
        return Session_exerciseService.get_session_exercise_data(session_exercisename)
