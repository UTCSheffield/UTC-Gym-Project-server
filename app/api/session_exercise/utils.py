def load_data(session_exercise_db_obj):
    """ Load session_exercise's data

    Parameters:
    - Session_exercise db object
    """
    from app.models.schemas import Session_exerciseSchema

    session_exercise_schema = Session_exerciseSchema()

    data = session_exercise_schema.dump(session_exercise_db_obj)

    return data
