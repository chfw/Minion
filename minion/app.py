import flask
from flask_cors import CORS

from minion.views import view


def create_app(static_folder=None, **conf):
    """
    Configure Flask application using the keywords from paster
    """
    app = flask.Flask("minion",
                      static_folder=static_folder,
                      static_url_path='/statics')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    CORS(app)
    app.register_blueprint(view)
    app.after_request(_add_allow_header)
    return app


def _add_allow_header(response):
    """Custom CORS header"""
    response.headers['Allow'] = 'HEAD, OPTIONS, POST, GET'
    return response
