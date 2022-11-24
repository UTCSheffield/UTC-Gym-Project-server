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
    bi = MuscleGroup(name="Biceps")
    db.session.add(bi)
    tri = MuscleGroup(name="Triceps") 
    db.session.add(tri)
    bp = Machine(name="Bench Press")
    db.session.add(bp)
    bp_exercise = Exercise(machine=bp, muscle_groups=[bi, tri], name="Bench Press", units="kg", how_to_use="with difficulty", default_reps=10, default_sets=3, default_value=10, default_perc_def=3)
    db.session.add(bp_exercise)


   

    ses = Session(location="UTC OLP", startDateTime=db.func.now(), endTime=db.func.now())
    bp_session_exercise = SessionExercise(exercise=bp_exercise, end=db.func.now(), reps=10, sets=3, value=10, perc_diff=3, units="kg")
    ses.exercises.append(bp_session_exercise)
   

    db.session.add(ses)

   
    db.session.add(bp_session_exercise)

    mes = Measurement(date=db.func.now(), height=174, resting_heartrate=60)
    us = User(email="bob@gmail.com", username="bob3", name="Bob Ross", password_hash="$2b$12$y9hO97HAn/9dbgYC.JCA9u2AMNh44YPGMAxjIDEXvrtB5LnkwOLq2")
    us.measurements.append(mes)
    db.session.add(mes)
    db.session.add(us)
    db.session.commit()

    return render_template("app/index.html")





    