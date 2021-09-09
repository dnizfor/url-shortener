import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask 



## SQLite Settings


app = Flask(__name__)

app.config["SECRET_KEY"] = "this_is_secret_key_19_xsz"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"


db = SQLAlchemy(app)




from . import routes
