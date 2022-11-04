from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

pwa_blueprint = Blueprint('pwa_blueprint', __name__, static_url_path="/", static_folder="../../UTC-Gym-Project-pwa" )
    
