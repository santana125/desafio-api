from . import manager_bp
from flask import render_template, jsonify

@manager_bp.route('/', methods=["GET"])
def index():
  return render_template('index.html')

@manager_bp.route('/list', methods=["GET"])
def list():
  return render_template('list.html')

@manager_bp.route('/show/<int:planet_id>', methods=["GET"])
def show(planet_id):
  return render_template('show.html', planet_id=planet_id)

@manager_bp.route('/create', methods=["GET"])
def create():
  return render_template('create.html')
