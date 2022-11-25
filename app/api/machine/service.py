from flask import current_app

from app.utils import err_resp, message, internal_err_resp
from app.models.machine import Machine


class MachineService:
    @staticmethod
    def get_machine_data(machinename):
        """ Get machine data by machinename """
        if not (machine := Machine.query.filter_by(name=machinename).first()):
            return err_resp("Machine not found!", "machine_404", 404)

        from .utils import load_data

        try:
            machine_data = load_data(machine)

            resp = message(True, "Machine data sent")
            resp["machine"] = machine_data
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
