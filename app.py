from flask import Flask
from config import Config
from models import db
from forms import csrf
from routes.main_routes import main_bp
from routes.wellness_routes import wellness_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        db.create_all()

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(wellness_bp, url_prefix="/wellness")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
