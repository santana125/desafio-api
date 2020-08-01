from flask import Flask

from .utils.database import db

from .api_v1 import api_v1_bp
from .manager import manager_bp

def create_app():
  from .utils.config import Config 
  app = Flask(__name__)
  app.config.from_object(Config)
  db.init_app(app)
  with app.app_context():
    db.create_all()  # Create database tables for our data models
    app.register_blueprint(api_v1_bp)
    app.register_blueprint(manager_bp, template_folder='templates')

    return app