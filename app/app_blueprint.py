from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from app import db
#from werkzeug.exceptions import aborts
from app.models.user import User, Role
from app.models.exercise import Exercise
from app.models.machine import Machine
from app.models.measurement import Measurement
from app.models.muscle_group import MuscleGroup
from app.models.session import Session
from app.models.session_exercise import SessionExercise

#app_blueprint = Blueprint('app_blueprint', __name__, static_url_path="app", static_folder="/home/meggleton/Projects/demo-progressive-web-app" )
app_blueprint = Blueprint('app_blueprint', __name__ )


@app_blueprint.route('/')
def index():
    return render_template("app/index.html")

@app_blueprint.route('/startvalues')
def startvalues():
    reset_database()

    bi = db.session.get(MuscleGroup, 1)
    if bi == None:
        bi = MuscleGroup(name="Biceps")
        db.session.add(bi)
    tri = db.session.get(MuscleGroup, 2)
    if tri == None:
        tri = MuscleGroup(name="Triceps") 
        db.session.add(tri)
    bp = db.session.get(Machine, 1)
    if bp == None:
        bp = Machine(name="Bench Press")
        db.session.add(bp)
    bp_exercise = db.session.get(Exercise, 1)
    if bp_exercise == None:
        bp_exercise = Exercise(machine=bp, muscle_groups=[bi, tri], name="Bench Press", units="kg", how_to_use="with difficulty", default_reps=10, default_sets=3, default_value=10, default_perc_def=3)
        db.session.add(bp_exercise)
    bp_session_exercise = db.session.get(SessionExercise, 1)
    if bp_session_exercise == None:
        bp_session_exercise = SessionExercise(exercise=bp_exercise, end=db.func.now(), reps=10, sets=3, perc_diff=3, units="kg", calories=10)
        db.session.add(bp_session_exercise)
    ses = db.session.get(Session, 1)
    if ses == None:
        ses = Session(location="UTC OLP", startDateTime=db.func.now(), endTime=db.func.now())
        ses.exercises.append(bp_session_exercise)
        ses.get_total_calories()
        db.session.add(ses)
    mes = db.session.get(Measurement, 1)
    if mes == None:
        mes = Measurement(date=db.func.now(), height=174, resting_heartrate=60, weight=70, age=20, sex="male")
        mes.calc_bmi()
        mes.calc_body_fat()
        db.session.add(mes)
    us = db.session.get(User, 1)
    if us == None:
        us = User(email="bob@gmail.com", username="bob3", name="Bob Ross", password_hash="$2b$12$y9hO97HAn/9dbgYC.JCA9u2AMNh44YPGMAxjIDEXvrtB5LnkwOLq2")
        us.measurements.append(mes)
        db.session.add(us)
    db.session.commit()

    return render_template("app/index.html")


def reset_database():
    db.session.query(Exercise).delete()
    db.session.query(Machine).delete()
    db.session.query(Measurement).delete()
    db.session.query(MuscleGroup).delete()
    db.session.query(SessionExercise).delete()
    db.session.query(Session).delete()
    db.session.query(User).delete()
    db.session.commit()


    


    