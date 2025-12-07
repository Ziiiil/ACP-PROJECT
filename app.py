from flask import Flask
from config import Config
from Models import db
from Forms import csrf
from Routes.main_routes import main_bp
from Routes.wellness_routes import wellness_bp
from Routes.event_routes import event_bp
from Routes.forum_routes import forum_bp

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
    app.register_blueprint(event_bp, url_prefix="/events")
    app.register_blueprint(forum_bp, url_prefix="/forum")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
