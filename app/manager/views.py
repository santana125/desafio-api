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

@manager_bp.route('/.well-know/assetlinks.json', methods=["GET"])
def android():
  return jsonify([{
  "relation": ["delegate_permission/common.handle_all_urls"],
  "target": {
    "namespace": "android_app",
    "package_name": "com.example.puppies.app",
    "sha256_cert_fingerprints":
    ["14:6D:E9:83:C5:73:06:50:D8:EE:B9:95:2F:34:FC:64:16:A0:83:42:E6:1D:BE:A8:8A:04:96:B2:3F:CF:44:E5"]
  }
  },])
