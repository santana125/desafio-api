from flask import Blueprint

manager_bp = Blueprint('manager', __name__, template_folder='templates', static_folder='../public')

from . import views