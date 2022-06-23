from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

def create_app():
    app = Flask(__name__)
    app.config["Secret Key"] = "Mysecret!"

    return app
