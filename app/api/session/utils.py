def load_data(session_db_obj):
    """ Load session's data

    Parameters:
    - Session db object
    """
    from app.models.schemas import SessionSchema

    session_schema = SessionSchema()

    data = session_schema.dump(session_db_obj)

    return data
