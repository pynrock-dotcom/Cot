import os

from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/')

    os.makedirs(app.instance_path, exist_ok=True)
    os.makedirs(os.path.join(app.static_folder, "img", "productos"), exist_ok=True)

    from app.blueprints.main import bp as main_bp

    app.register_blueprint(main_bp)
    return app
