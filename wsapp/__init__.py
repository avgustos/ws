# wsapp/__init__.py

import os
from flask import Flask, session
from flask_mail import Mail
from datetime import datetime

mail = Mail()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # make current_year available to all templates
    @app.context_processor
    def inject_year():
        return {'current_year': datetime.now().year}

    # Default configuration (safe defaults, no secrets here)
    app.config.from_mapping(
        SECRET_KEY='dev',  # ⚠️ change this in production
        DATABASE=os.path.join(app.instance_path, 'wsapp.sqlite'),
    )

    if test_config is None:
        # Load the instance config (contains MAIL settings, secrets, etc.)
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize Flask-Mail with loaded config
    mail.init_app(app)

    # ---- LANGUAGE SESSION HANDLER ----
    @app.before_request
    def set_default_language():
        if 'lang' not in session:
            session['lang'] = 'el'  # default language is Greek

    # ---- REGISTER BLUEPRINT ----
    from .routes import main
    app.register_blueprint(main)

    return app
