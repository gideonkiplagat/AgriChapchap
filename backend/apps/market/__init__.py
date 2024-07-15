from flask import Blueprint

market_blueprint = Blueprint('market', __name__)

from . import views
