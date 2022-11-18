from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import aborts
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
    db.session.add(MuscleGroup(name="Biceps"))
    db.session.add(MuscleGroup(name="Triceps"))
    db.session.commit()

    return render_template("app/index.html")





    