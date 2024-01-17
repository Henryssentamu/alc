from flask import Flask, redirect,request,render_template,url_for,flash, jsonify
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField,EmailField,PasswordField,SelectField
from wtforms.validators import ValidationError,DataRequired, EqualTo
import pycountry
# import sqlite3
import os

app = Flask("__name__")

try:
    serverSecratekey = os.environ['ALC_SERVER_SECRATE_KEY']
    app.config["SECRET_KEY"] = serverSecratekey
except KeyError as key:
    print(f"{key} this means that your secrate key does not exist, please work on it")
except Exception as keyerror:
    print(f"{keyerror}: investigate this error")


try:
    countryList = [(country.alpha_2, country.name )for country in pycountry.countries]
except Exception as error:
    print(f"{error}: check where you created country list! it wasn't generated ")



class RegistrationForm(FlaskForm):
    firstName = StringField(label="First Name",validators=[DataRequired(message="fill in your First Name")])
    sirName = StringField(label="Sir Name",validators=[DataRequired(message="fill in your Sir Name")])
    gender = SelectField(label="Gender",choices=[("male","Male"),("female","Female")],validators=[DataRequired(message="you must provide this")])
    country = SelectField(label="Country Of Origin", choices= countryList,validators=[DataRequired(message="fill in this as well")])
    phoneNumber = StringField(label="Phone Number",validators=[DataRequired(message="Enter your phone number")])
    email = EmailField(label="Your Email addres",validators=[DataRequired(message="invaled eamil addres")])
    password = PasswordField(label="Enter  Password",validators=[DataRequired(message="password required")])
    comfirmPassword = PasswordField(label="Comfirm  Password",validators=[DataRequired(message="password required")])

    submit = SubmitField()



class Authentication:
    def __init__(self):
        self.fName = None
        self.sName = None
        self.gender = None
        self.country = None
        self.phoneNumber = None
        self.email = None
        self.password = None
        
    def register(self):
        try:
            form = RegistrationForm()
            firstName = None
            sirName = None
            gender =None
            country = None
            phoneNumber = None
            email = None
            password = None
            comfirmPassword = None

            if form.validate_on_submit():
                """confirming that proper submissions are done."""
                firstName = form.firstName.data
                sirName = form.sirName.data
                gender = form.gender.data
                country = form.country.data
                phoneNumber = form.phoneNumber.data
                email = form.email.data
                password = form.password.data
                comfirmPassword = form.comfirmPassword.data
                
            
                
                try:
                    if password != comfirmPassword:
                        raise ValueError("password didn't match with confirm password")
                    else:
                        """ updating the class variable on submission"""
                        self.fName = firstName
                        self.sName = sirName
                        self.gender= gender
                        self.country = country
                        self.phoneNumber = phoneNumber
                        self.email = email
                        self.password = password

                        """the reset the feild to empty """
                        firstName = ""
                        sirName = ""
                        gender = ""
                        country = " "
                        phoneNumber = ""
                        email = " "
                        password = " "
                        comfirmPassword = " "
                except ValueError as passwordError:
                    raise ValueError(f"{passwordError}: investiaget this error but it must likely that the passwords didnt match")
                except Exception as other_error:
                    raise other_error
            return form
        except Exception as form_error:
            raise form_error
            



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

@app.route("/pythonCourse")
def pythonCourse():
    return render_template("coursePython.html")

@app.route("/introductionToPrograming")
def introductionToPrograming():
    return render_template("courseIntroductionToPrograming.html")


@app.route("/databaseManagementCourse")
def databaseManagementCourse():
    return render_template("courseSqlDatabase.html")

@app.route("/rProgramming")
def rProgrammingCourse():
    return render_template("courseRPrograming.html")

@app.route("/registrationPage", methods=["GET"])
def registrationPage():
    form_class = Authentication()
    form = form_class.register()
    return render_template("registrationPage.html",RegForm= form)





if __name__ == "__main__":
    app.run(debug=True)