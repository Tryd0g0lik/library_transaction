"""
Here is the run app of Flask and
USER's COMMAND of user's interface/ It's for create random of admin
"""
from typing import (Dict, Any)
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from werkzeug.routing import BaseConverter

from project.admins import admin_pannel
from dotenv_ import (SECRET_KEY, DSN, )


@admin_pannel()
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
    
    # CONFIG APP
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = DSN
    app.config["JWT_COOKIE_SECURE"] = True
    
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


flask_dict = create_flask
app_ = flask_dict["app"]
csrf = flask_dict["csrf"]
bcrypt = flask_dict["bcrypt"]
app_type = type(app_)


