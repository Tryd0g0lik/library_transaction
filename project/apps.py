"""
Here is the run app of Flask and
USER's COMMAND of user's interface/ It's for create random of admin
"""

from typing import Any, Dict

from flask import Flask
from flasgger import Swagger
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from werkzeug.routing import BaseConverter

# this is 'set()' the cloud for storage the book's registers.
register_key = set()

from dotenv_ import DSN, SECRET_KEY

def create_flask() -> Dict[str, Any]:
    """
    Creating the app flask
    :return:
    """

    class RegexConverter(BaseConverter):
        def __init__(self, url_map, regex):
            super(RegexConverter, self).__init__(url_map)
            self.regex = regex

    app = Flask(__name__, template_folder="templates")
    app.config.from_object(__name__)
    # SWAGGER
    swagger = Swagger(app, template="/swagger.yml")
    # CONFIG APP
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = DSN
    app.config["JWT_COOKIE_SECURE"] = True
    # app.config['SWAGGER'] =
    # Converter reg-expression
    app.url_map.converters["regex"] = RegexConverter
    # EXTENSIONS
    bcrypt = Bcrypt(app)
    bootstrap = Bootstrap(app)
    app.config["BOOTSTRAP"] = bootstrap
    csrf = CSRFProtect(app)
    
    
    
    # CREATE REDIS
    # redis_client = FlaskRedis()
    # REDIS INSTALL to the app
    # redis_client.init_app(app)
    return {
        "app": app,
        "csrf": csrf,
        "bcrypt": bcrypt,
    }


flask_dict = create_flask()
app_ = flask_dict["app"]
csrf = flask_dict["csrf"]

bcrypt = flask_dict["bcrypt"]
app_type = type(app_)

