from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_jwt_extended.exceptions import JWTExtendedException
from config import Config
from flask_cors import CORS
from flask import jsonify

db = SQLAlchemy()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.config["JWT_TOKEN_LOCATION"] = ["headers"]
    app.config["JWT_HEADER_NAME"] = "Authorization"
    app.config["JWT_HEADER_TYPE"] = "Bearer"
    app.config["PROPAGATE_EXCEPTIONS"] = True  # Helps with debugging

    jwt.init_app(app)
    CORS(app)

    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(tasks_bp, url_prefix="/tasks")

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"msg": "Resource not found"}), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"msg": "Bad request"}), 400
    
    @app.errorhandler(JWTExtendedException)
    def handle_jwt_error(e):
        return jsonify({"error": str(e)}), 422

    with app.app_context():
        db.create_all()

    return app

