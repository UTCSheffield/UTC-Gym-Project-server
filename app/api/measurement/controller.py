from flask_restx import Resource
from flask_jwt_extended import jwt_required

from .service import MeasurementService
from .dto import MeasurementDto

api = MeasurementDto.api
data_resp = MeasurementDto.data_resp


@api.route("/<string:measurementname>")
class MeasurementGet(Resource):
    @api.doc(
        "Get a specific measurement",
        responses={
            200: ("Measurement data successfully sent", data_resp),
            404: "Measurement not found!",
        },
    )
    @jwt_required()
    def get(self, measurementname):
        """ Get a specific measurement's data by their measurementname """
        return MeasurementService.get_measurement_data(measurementname)
