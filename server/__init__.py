import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
sql_uri = "sqlite:///" + os.path.join(basedir, "server.db")

app.config["SECRET_KEY"] = "CBgEgi0DNRnMQrwwYoFwa6MTwaEndIZQ"
app.config["SQLALCHEMY_DATABASE_URI"] = sql_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from server import models, views
