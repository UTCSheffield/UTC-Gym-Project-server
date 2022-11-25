from flask_restx import Resource
from flask_jwt_extended import jwt_required

from .service import SessionService
from .dto import SessionDto

api = SessionDto.api
data_resp = SessionDto.data_resp


@api.route("/<string:sessionname>")
class SessionGet(Resource):
    @api.doc(
        "Get a specific session",
        responses={
            200: ("Session data successfully sent", data_resp),
            404: "Session not found!",
        },
    )
    #@jwt_required()
    def get(self, sessionname):
        """ Get a specific session's data by their sessionname """
        return SessionService.get_session_data(sessionname)
