from flask import current_app

from app.utils import err_resp, message, internal_err_resp
from app.models.session import Session


class SessionService:
    @staticmethod
    def get_session_data(sessionname):
        """ Get session data by sessionname """
        if not (session := Session.query.filter_by(sessionname=sessionname).first()):
            return err_resp("Session not found!", "session_404", 404)

        from .utils import load_data

        try:
            session_data = load_data(session)

            resp = message(True, "Session data sent")
            resp["session"] = session_data
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
