from flask import current_app

from app.utils import err_resp, message, internal_err_resp
from app.models.session_exercise import SessionExercise


class Session_exerciseService:
    @staticmethod
    def get_session_exercise_data(session_exercisename):
        """ Get session_exercise data by session_exercisename """
        if not (session_exercise := SessionExercise.query.filter_by(name=session_exercisename).first()):
            return err_resp("Session_exercise not found!", "session_exercise_404", 404)

        from .utils import load_data

        try:
            session_exercise_data = load_data(session_exercise)

            resp = message(True, "Session_exercise data sent")
            resp["session_exercise"] = session_exercise_data
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
