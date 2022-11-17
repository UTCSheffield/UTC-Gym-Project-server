from flask_restx import Resource
from flask_jwt_extended import jwt_required

from .service import ExerciseService
from .dto import ExerciseDto

api = ExerciseDto.api
data_resp = ExerciseDto.data_resp


@api.route("/<string:exercisename>")
class ExerciseGet(Resource):
    @api.doc(
        "Get a specific exercise",
        responses={
            200: ("Exercise data successfully sent", data_resp),
            404: "Exercise not found!",
        },
    )
    @jwt_required()
    def get(self, exercisename):
        """ Get a specific exercise's data by their exercisename """
        return ExerciseService.get_exercise_data(exercisename)
