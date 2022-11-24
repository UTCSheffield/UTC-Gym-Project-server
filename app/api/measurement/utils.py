def load_data(measurement_db_obj):
    """ Load measurement's data

    Parameters:
    - Measurement db object
    """
    from app.models.schemas import MeasurementSchema

    measurement_schema = MeasurementSchema()

    data = measurement_schema.dump(measurement_db_obj)

    return data
