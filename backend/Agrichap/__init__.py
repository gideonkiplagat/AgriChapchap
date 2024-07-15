from flask import Flask
from .settings import Config  # Import your configuration settings
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)
    migrate.init_app(app, db)

    # Import blueprints
    from .apps.users.views import users_bp
    from .apps.market.views import market_bp

    # Register blueprints
    app.register_blueprint(users_bp)
    app.register_blueprint(market_bp)

    return app
