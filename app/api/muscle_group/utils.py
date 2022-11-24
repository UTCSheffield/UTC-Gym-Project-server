def load_data(muscle_group_db_obj):
    """ Load muscle_group's data

    Parameters:
    - Muscle_group db object
    """
    from app.models.schemas import Muscle_groupSchema

    muscle_group_schema = Muscle_groupSchema()

    data = muscle_group_schema.dump(muscle_group_db_obj)

    return data
