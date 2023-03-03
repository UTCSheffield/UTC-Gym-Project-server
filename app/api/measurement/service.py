from flask import current_app

from app.utils import err_resp, message, internal_err_resp
from app.models.measurement import Measurement


class MeasurementService:
    @staticmethod
    def get_measurement_data(measurementname):
        """ Get measurement data by measurementname """
        if not (measurement := Measurement.query.filter_by(name=measurementname).first()):
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

    @staticmethod
    def retrieve(measurementname):
        return get_measurement_data(measurementname)

    @staticmethod
    def create(data):
        # Assign vars

        ## Required values
        height = data["height"]
        weight = data["weight"]
        restingHeartrate = data["resting heartrate"]

        ## Optional
        data_name = data.get("name")

        try:
            new_user = User(
                email=email,
                username=username,
                name=data_name,
                password=password,
                joined_date=datetime.utcnow(),
            )

            db.session.add(new_user)
            db.session.flush()

            # Load the new user's info
            user_info = user_schema.dump(new_user)

            # Commit changes to DB
            db.session.commit()

            # Create an access token
            access_token = create_access_token(identity=new_user.id)

            resp = message(True, "User has been registered.")
            resp["access_token"] = access_token
            resp["user"] = user_info

            return resp, 201

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()