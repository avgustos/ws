# wsapp/__init__.py

import os
from flask import Flask, session

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',  # change to something secure in production
        DATABASE=os.path.join(app.instance_path, 'wsapp.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # ---- LANGUAGE SESSION HANDLER ----
    @app.before_request
    def set_default_language():
        if 'lang' not in session:
            session['lang'] = 'el'  # default language is Greek

    # ---- REGISTER BLUEPRINT ----
    from .routes import main
    app.register_blueprint(main)

    return app
