from flask import Flask, redirect,request,render_template,url_for,flash, jsonify
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField,EmailField,PasswordField
from wtforms.validators import ValidationError,DataRequired, EqualTo
# import sqlite3
import os

serverSecratekey = os.environ['ALC_SERVER_SECRATE_KEY']
app = Flask("__name__")
app.config["SECRET_KEY"] = serverSecratekey

@app.route("/")
def homePage():
    return render_template("homePage.html")

@app.route("/schoolSoftwareEngineering")
def schoolSoftwareEngineering():
    return render_template("softwareEngineeringSchool.html")

@app.route("/schoolDataScience")
def schoolDataScience():
    return render_template("dataScienceSchool.html")

@app.route("/admissionDetails")
def admissionDetails():
    return render_template("admissionPolicy.html")

@app.route("/aboutUs")
def aboutUsPage():
    return render_template("aboutUs.html")

if __name__ == "__main__":
    app.run(debug=True)