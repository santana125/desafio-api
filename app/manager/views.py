from . import manager_bp
from flask import render_template

@manager_bp.route('/', methods=["GET"])
def index():
  return render_template('index.html')