from flask import current_app

from app.utils import err_resp, message, internal_err_resp
from app.models.measurement import Measurement


class MeasurementService:
    @staticmethod
    def get_measurement_data(measurementname):
        """ Get measurement data by measurementname """
        if not (measurement := Measurement.query.filter_by(measurementname=measurementname).first()):
            return err_resp("Measurement not found!", "measurement_404", 404)

        from .utils import load_data

        try:
            measurement_data = load_data(measurement)

            resp = message(True, "Measurement data sent")
            resp["measurement"] = measurement_data
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
