from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/Test"
app.config["SECRET_KEY"]="secret"


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
