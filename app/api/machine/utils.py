def load_data(machine_db_obj):
    """ Load machine's data

    Parameters:
    - Machine db object
    """
    from app.models.schemas import MachineSchema

    machine_schema = MachineSchema()

    data = machine_schema.dump(machine_db_obj)

    return data
