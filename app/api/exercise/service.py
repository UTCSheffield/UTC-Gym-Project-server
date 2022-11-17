from flask import current_app

from app.utils import err_resp, message, internal_err_resp
from app.models.exercise import Exercise


class ExerciseService:
    @staticmethod
    def get_exercise_data(exercisename):
        """ Get exercise data by exercisename """
        if not (exercise := Exercise.query.filter_by(name=exercisename).first()):
            return err_resp("Exercise not found!", "exercise_404", 404)

        from .utils import load_data

        try:
            exercise_data = load_data(exercise)

            resp = message(True, "Exercise data sent")
            resp["exercise"] = exercise_data
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
