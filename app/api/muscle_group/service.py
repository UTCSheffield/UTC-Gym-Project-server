from flask import current_app

from app.utils import err_resp, message, internal_err_resp
from app.models.muscle_group import MuscleGroup


class Muscle_groupService:
    @staticmethod
    def get_muscle_group_data(muscle_groupname):
        """ Get muscle_group data by muscle_groupname """
        if not (muscle_group := MuscleGroup.query.filter_by(name=muscle_groupname).first()):
            return err_resp("Muscle_group not found!", "muscle_group_404", 404)

        from .utils import load_data

        try:
            muscle_group_data = load_data(muscle_group)

            resp = message(True, "Muscle_group data sent")
            resp["muscle_group"] = muscle_group_data
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
