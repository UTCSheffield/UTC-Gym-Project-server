def load_data(exercise_db_obj):
    """ Load exercise's data

    Parameters:
    - Exercise db object
    """
    from app.models.schemas import ExerciseSchema

    exercise_schema = ExerciseSchema()

    data = exercise_schema.dump(exercise_db_obj)

    return data
