


from ast import Not, Pass
from crypt import methods
import json
from flask import Flask, render_template,request,redirect, session,url_for,jsonify,flash
from flask.cli import routes_command
from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin,login_user,login_required,logout_user,current_user
from wtforms import SelectField,StringField,SubmitField,EmailField,PasswordField
from wtforms.validators import DataRequired
import pycountry
import os
import sqlite3
from databases import PartnershipDatabase, ExamStudentAnswes, Exams, Courses, StudentCourseProjectRepoDetails,SchoolDatabes,StudentCourseProject ,Test,TestStudentAnswes,AssessmentResults, StudentDatabases, EnrolledInCourses, FetchStudentData, LiveSessions,ExamStudentAnswes, CoursePaymentsDataDase,SchoolDatabes,formateSchoolData
from createStudentId import CreatePaperIds, CreateStudentId, GenerateProjectId
from saikoleearnApis import CourseDetailsApi, AdminCredientalApi,StudentApi,SchoolApi
# from fetchCoursesApi import CourseDetailsApi
# from adminApi import AdminCredientalApi
# from studentDetailsApi import StudentApi
# from createPaymentRefrenceNumber import GenerateCoursePaymentRefrenceNumber
from authentication import GetStudent
from envKeys import strip_key,stripwhookkey,saikolearn_SECURITY
import stripe
from sendemail import sendEmail,SendPartnershipEmails,SendInqurry






app = Flask("__name__")
login_manager = LoginManager()
login_manager.init_app(app)

YOUR_DOMAIN = 'https://saikolearn.org'
stripe.api_key = strip_key
# stripe.Product.create(name="database")
# stripe.Price.create(
#   product='{{PRODUCT_ID}}',
#   unit_amount=2000,
#   currency="usd",
# )

try:
    security = saikolearn_SECURITY
    app.config["SECRET_KEY"] = security

except ValueError as error:
    print(f"set App secrat key:{error} ")
except Exception as error:
    print(f"app secrat key is not set. in the termino type export{error} =  set your key here" )

def getCountries():
    return [(country.alpha_2, country.name)for country in pycountry.countries]
available_schools = [("datascience","School of Data Science"),("softwareEngineering", "School of Software Engineering")]
intake_list = [("cohort1","cohort1 (January-intake)"),("cohort2","cohort2 (Apirl in-tak)"),("cohort3","cohort3 (August in-take)"),("cohort4","cohort4 (December in-tak)")]


class RegistrationFormStructure(FlaskForm):
    firstName = StringField(label="First Name",validators=[DataRequired(message="fill in your First Name")])
    sirName = StringField(label="Sir Name",validators=[DataRequired(message="fill in your Sir Name")])
    gender = SelectField(label="Gender",choices=[("male","Male"),("female","Female")],validators=[DataRequired(message="you must provide this")])
    country = SelectField(label="Country Of Origin", choices= getCountries(),validators=[DataRequired(message="fill in this as well")])
    phoneNumber = StringField(label="Phone Number",validators=[DataRequired(message="Enter your phone number")])
    email = EmailField(label="Your Email addres",validators=[DataRequired(message="invaled eamil addres")])
    password = PasswordField(label="Enter  Password",validators=[DataRequired(message="password required")])
    comfirmPassword = PasswordField(label="Comfirm  Password",validators=[DataRequired(message="password required")])
    schools = SelectField(label="Select School",choices= available_schools)
    intake = SelectField(label="Choose in-take cohort", choices=intake_list)
    submit = SubmitField(label= "Submit")

class StudentLoginForm(FlaskForm):
    studentId = StringField(label=" Your Student Id", validators=[DataRequired(message="It's a must")])
    password = PasswordField(label="Your Password",validators=[DataRequired(message="you should provide this")])
    submit = SubmitField()
class AdminLoginForm(FlaskForm):
    employeeId = StringField(label="Employee ID Number", validators=[DataRequired(message="It's a must")])
    adminCode = StringField(label="Admin Code", validators=[DataRequired(message="It's a must")])
    password = PasswordField(label="Your Password",validators=[DataRequired(message="you should provide this")])
    submit = SubmitField()

class PartnerForm(FlaskForm):
    firstName = StringField(label="First Name",validators=[DataRequired(message="fill in your First Name")])
    sirName = StringField(label="Sir Name",validators=[DataRequired(message="fill in your Sir Name")])
    country = SelectField(label="Country Of Origin", choices= getCountries(),validators=[DataRequired(message="fill in this as well")])
    phoneNumber = StringField(label="Phone Number",validators=[DataRequired(message="Enter your phone number")])
    email = EmailField(label="Your Email addres",validators=[DataRequired(message="invaled eamil addres")])
    current_affriation = StringField(label="Organization/Company (if any)")
    position = StringField(label="Position/Title")
    investment_amount = StringField(label="Investment Amount (USD)")
    type_of_partnernship = SelectField(label="Type of partnership",choices=[("options","choose the type"),("grant","Grant Partner"),("corporate_ally","Corporate Ally")])
    purpose_of_partnership = StringField(label="Purpose of Financial Partnership ")
    expection_from_partnership = StringField(label="Expected Benefits or Returns from the Partnership (if any):")
    more_info = StringField(label="Is there anything else you would like us to know about your interest in  partnership with saikolearn? ")

    submit = SubmitField()



class CoursePaymentDetails(FlaskForm):
    fullNames = StringField(label="Your Full Names",validators=[DataRequired(message="fill in your Full Name")])
    studentId = StringField(label="Student Id Number",validators=[DataRequired(message="you Must provide your Student Id number")])
    PhoneNumber = StringField(label="Phone Number",validators=[DataRequired(message="Provide your phone number")])
    email = EmailField(label="Your Email addres",validators=[DataRequired(message="invaled eamil addres")])
    submit = SubmitField(label= "Submit")



class User(UserMixin):
    def __init__(self,id):
        super().__init__()
        self.id = id


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)



# creation on exam database and insertation but this should be done on admins route when created

questions = [
    {
        "question": "What is the process of converting raw data into a more structured format called?",
        "options": [
          "Data Visualization",
          "Data Wrangling",
          "Data Mining",
          "Data Aggregation"
        ],
        "correct_answer": "Data Wrangling"
      },
      {
        "question": "Which of the following is NOT a supervised learning algorithm?",
        "options": [
          "Linear Regression",
          "Decision Tree",
          "K-Means Clustering",
          "Support Vector Machine"
        ],
        "correct_answer": "K-Means Clustering"
      },
      {
        "question": "What statistical measure is used to quantify the dispersion or spread of a dataset?",
        "options": [
          "Mean",
          "Median",
          "Mode",
          "Standard Deviation"
        ],
        "correct_answer": "Standard Deviation"
      }
    ]

# test question sample

testQuestions = [
    {
        "question": "What is the process of converting raw data into a more structured format called?",
        "options": [
          "Data Visualization",
          "Data Wrangling",
          "Data Mining",
          "Data Aggregation"
        ],
        "correct_answer": "Data Wrangling"
      },
      {
        "question": "Which of the following is NOT a supervised learning algorithm?",
        "options": [
          "Linear Regression",
          "Decision Tree",
          "K-Means Clustering",
          "Support Vector Machine"
        ],
        "correct_answer": "K-Means Clustering"
      },
      
    ]







@app.route("/")
def homePage():
    return render_template("homePage.html")

@app.route("/schoolSoftwareEngineering", methods =["GET","POST"])
def schoolSoftwareEngineering():
    if request.method == "GET":
        requestType = request.args.get("type")
        if requestType == "availableCourses":
            # courseIdObj = {"schoolId": "SOSE"}
            # coureses = FetchAvaibleCourses(object=courseIdObj)
            # data = coureses.availabCourses()
            courses = CourseDetailsApi()
            data = courses.fetchAvaibleCourses(schoolId="SOSE")
            data = [{"courseId":obj[0], "schoolId":obj[1], "coursName":obj[2],  "courseDuration":obj[3], "routeFunction":obj[4],"tuition":obj[5], "priceId":obj[6],"courseImage":obj[7], "courseDiscription":obj[8]} for obj in data ]
            return jsonify({"data":data})
    return render_template("softwareEngineeringSchool.html")

@app.route("/schoolDataScience")
def schoolDataScience():
    requestType = request.args.get("type")
    if requestType == "availableCourses":
        # coureses = CourseDetailsApi()
        # data = coureses.fetchAvaibleCourses(schoolId= "SODS")
        courses = CourseDetailsApi()
        data = courses.fetchAvaibleCourses(schoolId="SODS")
        data = [{"courseId":obj[0], "schoolId":obj[1], "coursName":obj[2],  "courseDuration":obj[3], "routeFunction":obj[4],"tuition":obj[5], "priceId":obj[6],"courseImage":obj[7], "courseDiscription":obj[8]} for obj in data ]
        # print(data)
        return jsonify({"data":data})
    return render_template("dataScienceSchool.html")

@app.route("/admissionDetails")
def admissionDetails():
    return render_template("admissionPolicy.html")

@app.route("/aboutUs")
def aboutUsPage():
    return render_template("aboutUs.html")

@app.route("/contact", methods=["POST","GET"])
def contactPage():
    if request.method == "POST":
        requesttype = request.json.get("type")
        if requesttype == "inquiry":
            inquiryData = request.json.get("data")
            """ send message to saikolearn webmail """
            if inquiryData:
                inquiryObject = SendInqurry(inqurryDetails=inquiryData)
                inquiryObject.sendInquery()
            return jsonify({"inquryResponse":" inqury message recieved"})
    elif request.method == "GET":
        pass
        
    return render_template("contactPage.html")

@login_required
@app.route("/pythonCourse")
def pythonCourse():
    if not current_user.is_authenticated:
        session["pythonCourse"] = request.url
        return redirect(url_for('login'))
    return render_template("coursePython.html")

@login_required
@app.route("/introductionToPrograming")
def introductionToPrograming():
    if not current_user.is_authenticated:
        session["introToProgramming"] = request.url
        return redirect(url_for('login'))
    return render_template("courseIntroductionToPrograming.html")

@login_required
@app.route("/databaseManagementCourse")
def databaseManagementCourse():
    if not current_user.is_authenticated:
        session["DBMSurl"] = request.url
        return redirect(url_for('login'))
    return render_template("courseSqlDatabase.html")

@login_required
@app.route("/rProgramming")
def rProgrammingCourse():
    if not current_user.is_authenticated:
        session["rprograming"] = request.url
        return redirect(url_for('login'))

    return render_template("courseRPrograming.html")


@app.route("/onlinetests")
def onlinetests():
    return render_template("onlineTestPage.html")

@app.route("/onlineexam")
def onlineexam():

    return render_template("exampage.html")

@app.route("/recordedSessions")
def recordedSessions():

    return render_template("recordedSessions.html")

@app.route("/studentScores")
def studentScores():

    return render_template("studentscores.html")

@app.route("/projectpage", methods = ["POST","GET"])
def projectPage():
    if request.method == "POST":
        postType = request.json.get("type")
        if postType == "fromadmin":
            data = request.json.get("data")
            if data:
                courseId = data["courseId"]
                cohort = data["cohort"]
                projectDetails = data["projectDetails"]
                projectDetailsFormated = json.loads(projectDetails)

                """get project id """

                projectIdObject = GenerateProjectId(courseId=courseId,cohort=cohort)
                projectId = projectIdObject.projectid()

                projectObject = StudentCourseProject(projectObject=projectDetailsFormated,cohort=cohort,courseId=courseId,projectId=projectId)
                projectObject.createTables()
                projectObject.insertIntoTable()
                
                return jsonify({"project status":"recieved"})
        elif postType == "ProjectRepo":
            data = request.json.get("data")
            if data:
                studentId = current_user.id
                ProjectRepo = data

                repoObject = StudentCourseProjectRepoDetails(reponseObject=ProjectRepo,studentId=studentId)
                repoObject.createTable()
                repoObject.inserIntotable()
                return jsonify({"status":"project rep recieved"})
            else:
                return jsonify({"status":"Norep"})
    elif request.method == "GET":
        getType = request.args.get("type")
        if getType == "projectInstruction":
            courseDetails = session.get("courseDetails_loadedOnStudentPortal")
            cohort = courseDetails["cohort"]
            courseId = courseDetails["courseId"]
            try:
                with sqlite3.connect("CourseProjectInstructions.db") as db:
                    cursor = db.cursor()
                    cursor.execute("""
                        SELECT
                            ProjectId,
                            CourseId,
                            Cohort,
                            ProjectTitle,
                            ProjectDescription,
                            Deadline,
                            StartDate
                        FROM
                            projectDetails
                        WHERE
                            CourseId ==? AND Cohort== ?
                            
                    
                            
                                   
                    """,(courseId,cohort))
                    data = cursor.fetchone()
                if data:
                    return jsonify({"data":data})
                else:
                    return jsonify({"status":"NO PROJECT SET YET"})
            except sqlite3.Error as e:
                raise RuntimeError(f"connection error on course project instruction db:{e}")
            except Exception as e:
                raise RuntimeError(f"faced error while accessing course project instruction db: {e}") 



    return render_template("projectPage.html")

@app.route("/livesessionLink")
def livesessionLink():

    return render_template("liveSessionPage.html")


@app.route("/registrationPage", methods=["GET","POST"])
def registrationPage():
    form = RegistrationFormStructure()
    try:
        fName = None
        sName = None
        pnumber = None
        emailAddress = None
        countryOfOrigin  = None
        studentGender = None
        studentPassword = None
        comfirmPassword = None
        schoolOfAttachment = None
        intakeChoosen = None
        
        if form.validate_on_submit():
            """populating function variables"""
            firsNname = form.firstName.data
            sirName = form.sirName.data
            number = form.phoneNumber.data
            email = form.email.data
            country = form.country.data
            gender = form.gender.data
            school = form.schools.data
            password = form.password.data
            comfirm = form.comfirmPassword.data
            intake =  form.intake.data
            """ asigning  form variable to function variable """
            fName = firsNname
            sName = sirName
            pnumber = number
            emailAddress = email
            countryOfOrigin  = country
            studentGender = gender
            studentPassword = password
            comfirmPassword = comfirm
            schoolOfAttachment = school
            intakeChoosen = intake
            try:
                if comfirmPassword == studentPassword:
                    """re initialize the form variable to empty string  so that when a person leaves the registration page, on re accessing it, it be empty"""
                    firsNname = ""
                    sirName = ""
                    number = ""
                    email = ""
                    country = ""
                    gender = ""
                    school = ""
                    password = ""
                    comfirm = ""
                    intake = ""

                    """creating database object """
                    #making student id 
                    try:
                        student = CreateStudentId()
                        studentId = student.makeStudentId()
                    except ValueError as error:
                        print(f" probably create student id class failed. check the error: {error}")
                    #create database 
                    studentDataBase = StudentDatabases(studentId= studentId ,firstname=fName,sirName=sName,gender=studentGender,phoneNumber=pnumber,email=emailAddress,school=schoolOfAttachment,password=studentPassword,intake=intakeChoosen,country=countryOfOrigin,)

                    """ creating tables """
                    studentDataBase.createTables()
                    """inserting values into the created tables"""
                    studentDataBase.insertIntoTables()
                    # print(emailAddress,studentId,password)

                    """send student login details to their email"""
                    
                    sendEmail(Email=emailAddress, sPassword=studentPassword, studentRigNo=studentId)
                    return redirect(url_for('checkYourLoginCredentials'))
                else:
                    return redirect(url_for('registrationPage'))
            except ValueError as error:
                raise RuntimeError(f"possibly password did not match or student database wasnt properly created. check the error:{error}")
        else:
            print(f"the submit button on the form has issues: {form.errors}")
    except Exception as error:
        print(f"the register form structure call failed: {error}")
    
    return render_template("registrationPage.html",RegForm= form)

@app.route("/checkYourLoginCredentials")
def checkYourLoginCredentials():
    return render_template("checkYourLoginCredentials.html")


@app.route("/registerPartners",methods=["GET","POST"])
def registerPartners():
    form = PartnerForm()
    try:
        firstName = None
        sirName = None
        number = None
        email = None
        country  = None
        affriation = None
        position = None
        investment_amount = None
        type_of_partnernship = None
        purpose_of_partnership = None
        expection_from_partnership = None
        more_info = None
        
        if form.validate_on_submit():
            """populating function variables"""
            firstName = form.firstName.data
            sirName = form.sirName.data
            number = form.phoneNumber.data
            email = form.email.data
            country = form.country.data
            affriation = form.current_affriation.data
            position = form.position.data
            investment_amount = form.investment_amount.data
            type_of_partnernship = form.type_of_partnernship.data
            purpose_of_partnership =  form.purpose_of_partnership.data
            expection_from_partnership = form.expection_from_partnership.data
            more_info = form.more_info.data

           

            if firstName and sirName and email and number:
                
                PartnershipData = {"firstName":firstName, "sirName":sirName,"phoneNumber":number,"email": email, "country":country,"typeOfPartnership":type_of_partnernship}
                PartnershipMessageData = {
                    "moreInfo":more_info,
                    "expectionFromPartnership":expection_from_partnership,
                    "affriation": affriation,
                    "position": position,
                    "funding":investment_amount,
                    "purposeOfpartnership": purpose_of_partnership,
                    "firstName":firstName, 
                    "sirName":sirName,
                    "phoneNumber":number,
                    "email": email, 
                    "country":country,
                    "typeOfPartnership":type_of_partnernship
                    }

                try:
                    """ populating partnership database """
                    partnershipObject = PartnershipDatabase(dataObject= PartnershipData)
                    partnershipObject.CreateTables()
                    partnershipObject.insertIntoTable()
                    try:
                        """sending partner's details to saikolearn webmail and thanks message to partner """
                        messageObject = SendPartnershipEmails(partnersDetails= PartnershipMessageData)
                        #sends to acl
                        messageObject.sendPartnersDetailsTo_saikolearn_account()
                        #sends to partner
                        messageObject.sendMessageReceivedResponseToPartner()
                        return redirect(url_for('thankyouPartner'))
                    except Exception as error:
                        raise RuntimeError(f"error while send partner's details to emails: {error}")

                    # will handle sending emails to both the partner and to the saikolearn webmail account
                except Exception as error:
                    raise RuntimeError(f"error while calling partnership db:{error}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
            """re initailise the function variable so that when a person leaves the registration page, on re accessing it, it be empty"""

            firstName = ""
            sirName = ""
            number = ""
            email = ""
            country  = ""
            affriation = ""
            position = ""
            investment_amount = ""
            type_of_partnernship = ""
            purpose_of_partnership = ""
            expection_from_partnership = ""
            more_info = ""
        else:
            print(f"the submit button on the form has issues: {form.errors}")
    except Exception as error:
        raise RuntimeError(f"the register form structure call failed: {error}")
    
    return render_template("partnerPage.html", form=form)


@app.route("/thankyouPartner")
def thankyouPartner():
    return render_template("thankyouPartner.html")


@app.route("/login", methods=["GET","POST"])
def login():
    form = StudentLoginForm()

    try:
        if form.validate_on_submit():
            studentId = form.studentId.data
            password = form.password.data
        #    Getstudent is a class that returns TRue if the provided student credentials are correct 
            checkCredentials = GetStudent(studentId= studentId, password=password)
            is_student = checkCredentials.is_authenticated()
            if is_student:
                user = User(studentId)
                
                loginStatus = login_user(user=user)
                if loginStatus:
                    if "DBMSurl" in session:
                        referrer = session.pop("DBMSurl",None)
                    elif "pythonCourse" in session:
                        referrer = session.pop("pythonCourse",None)
                    elif "introToProgramming" in session:
                        referrer = session.pop("introToProgramming", None)
                    elif "rprograming" in session:
                        referrer = session.pop("rprograming",None)
                    elif "payment_url" in session:
                        referrer = session.pop("payment_url")
                    else:
                        referrer = False
                    
                    if referrer:
                        return redirect(referrer)
                    else:
                        return redirect(url_for('studentDashboard'))  
                return redirect(url_for('login'))
            return redirect(url_for('failedTologinStudent'))
    except Exception as error:
        raise RuntimeError(f"possibility that student login class didnt work:{error}")
    return render_template("studentLogin.html",form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('homePage'))

@app.route("/adminLogin", methods=["POST","GET"])
def adminLogin():
    form = AdminLoginForm()
    try:
        if form.validate_on_submit():
            employeeId = form.employeeId.data
            adminCode = form.adminCode.data
            password = form.password.data
            data =  {'employeeId': employeeId, 'admincode': adminCode, 'password': password}

            """check where admin exists"""
            obj = AdminCredientalApi(adminObject= data)
            response = obj.is_admin()
            if response:
                employeId = employeeId
                user = User(id= employeId)
                login_user(user= user)
                nexUrl = session.pop("admin_referrer",None)
                return redirect(nexUrl or url_for('admin'))
            else:
                return redirect(url_for("failedTologinAdmin"))
    except Exception as e:
        raise RuntimeError(f"error in logging in admin:{e}")
    return render_template("adminlogin.html", form=form)

@app.route("/failedTologinAmin")
def failedTologinAdmin():
    return render_template("failedTologinAdmin.html")
@app.route("/failedTologinStudent")
def failedTologinStudent():
    return render_template("failedTologinStudent.html")

@login_required
@app.route("/studentDashboard", methods = ["POST","GET"])
def studentDashboard():
    
    return render_template("studentDashboard.html")

@login_required
@app.route("/payments",methods=["POST","GET"])
def payment():
    if not current_user.is_authenticated:
        # this url is used in login route to determin whether user was redirected from here,so that after 
        # loging in is redirected back 
        session["payment_url"] = request.url
        return redirect(url_for('login'))
    try:
        details= session.get("enrolledCourseDetails")
        priceID = details["priceId"]
        if priceID:

            session["studentPaidCourseDetails"] = {"studentId":current_user.id, "courseId":details["courseID"]}
            try:   
                checkout_session = stripe.checkout.Session.create(
                    line_items=[
                        {
                            # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                            'price': priceID,
                            'quantity': 1,
                        },
                    ],
                    mode='payment',
                    success_url=YOUR_DOMAIN + '/OnsuccesfullPayment',
                    cancel_url=YOUR_DOMAIN + '/login'
                )
            except Exception as error:
                raise RuntimeError(f"error related to strip checkout page: {error}")
    except Exception as e:
        raise RuntimeError(f"error in payment route:{e}")
                
    return redirect(checkout_session.url,code=303)


# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
# # This is your Stripe CLI webhook secret for testing your endpoint locally.

endpoint_secret = stripwhookkey

""" here will handle webhook such that, i triger add course to a student's portal accout
    after the payment hass been successfuly made.
"""



@app.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.data
    sig_header = request.headers['STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        raise RuntimeError(e) 
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
         raise RuntimeError(e)

    # Handle the event
    if event['type'] == 'checkout.session.async_payment_failed':
      session = event['data']['object']
      print(session)
    elif event['type'] == 'checkout.session.async_payment_succeeded':
      session = event['data']['object']

      """on successfull payment 
        redirect to payment recieved route where enrolled in courses database is populated
      """
      return redirect(url_for('paymentRecieved'))
    elif event['type'] == 'checkout.session.completed':
      session = event['data']['object']
    #   print(session)
    elif event['type'] == 'checkout.session.expired':
      session = event['data']['object']
      print(session)
    # ... handle other event types
    else:
      print('Unhandled event type {}'.format(event['type']))

    return jsonify(success=True)

@app.route("/OnsuccesfullPayment")
def OnsuccesfullPayment():
    return render_template("successfulPaymentMessage.html")


    



@app.route("/processDataForEnrolledCourse",methods=["POST","GET"])
def processDataForEnrolledCourse():
    try:
        if request.method == "POST":
            postType = request.json.get("type")
            if postType and postType == "courseIdDetails":
                courseId = request.json.get("data")

                """check payment details of the course to enroll to"""
                paymentObject = CourseDetailsApi()
                paymentDetails = paymentObject.courseTuitionDetails(courseId= courseId)
                price = paymentDetails['price']

                if isinstance(price, int) and price != 0:
                    priceID = paymentDetails["priceId"]
                    """ if the course is a paid course, user is redirected to strip checkout page"""
                    session["enrolledCourseDetails"] = {"courseID":courseId,"priceId":priceID}
                else:
                    
                    try:
                        """ this means that the course is free, therefore the  enrolled in course database is populated 
                        with student and course details
                        """
                        studentId = current_user.id
                        courseID = courseId 
                        paymentData = EnrolledInCourses(studentId= studentId, courseId= courseID)
                        paymentData.createTables()
                        paymentData.insertIntoTables()
                    except Exception as error:
                        raise RuntimeError(f" possibilies of user not being registered:{error}")
            return jsonify({"responseStatus":"ok"})
    except Exception as error:
        raise RuntimeError(f" error in processing enrolled course:{error}")




    

@app.route("/studentPaidCourseRecords")
def paymentRecieved():
    """ this route handles all paid course.
        On successful payment, the enrolled in course database is populated 
        in the webhook
    """
    try:
        paidCourseDetails = session.get("studentPaidCourseDetails")
    except Exception as error:
        raise RuntimeError(f"error while accessing paid course details session: {error}")
    if paidCourseDetails:
        studentId = paidCourseDetails["studentId"]
        courseId = paidCourseDetails["courseId"]
        try:
            paymentData = EnrolledInCourses(studentId= studentId, courseId= courseId)
            paymentData.createTables()
            paymentData.insertIntoTables()
        except Exception as error:
            raise RuntimeError(f"error while populating purchased course database:{error}")

    




@app.route("/continueTodStudentDashBoard")
def continueTodStudentDashBoard():
    return render_template("continueToStudentDashboard.html")







@app.route("/getBioDataAndCourseDetails", methods= ["GET","POST"])
def getBioDataAndCourseDetails():
    if request.method == "GET":
        details = []
        """
            bellow we are accessing student bio data by initailizing student object then call studentBio function
        """
        # studentId = session.get("logged_student_id")
        studentId = current_user.id
                
        student  = FetchStudentData(studentId= studentId)
        studentData = student.studentBio()
        # print(f"fatched student data:{studentData}")
        try:
            """
                this api sends student bio data and course details on each login session which are to be rendered
                on student portal. so it sends those details to a js file which handle rendering 
                html content on student portal
            """
            with sqlite3.connect("EnrolledInCourses.db") as db:
                curser = db.cursor()
                curser.execute("""
                    SELECT DISTINCT
                        c.CourseId
                    FROM
                        purchasedCourse as c
                    WHERE
                        c.StudentId == ?   
                """,(studentId,))
                purchased_course = curser.fetchall()
            
            # print(f"yes he bought this course:{purchased_course}")
            if purchased_course:
                courseList = [ courseid[0] for courseid in purchased_course]
                # print(f"course list here: {courseList}")

                for id in courseList:
                    try:
                        with sqlite3.connect("courseDatabase.db") as db:
                            cursor = db.cursor()
                            cursor.execute("""
                                SELECT
                                    C.courseId,C.courseName, I.courseImageLink
                                FROM
                                    courseDetails AS C
                                JOIN
                                    courseImageLinks AS I ON I.courseId == C.courseId
                                WHERE
                                    C.courseId == ?
                            """, (id,))
                            details.append(cursor.fetchone())
                    except sqlite3.Error as error:
                        raise RuntimeError(f"error in accessing course database in login route:{error}")
                # print(details)
                
                
        except sqlite3.Error as error:
            raise RuntimeError(f"failed to connect to sqlite in the login route:{error}")
        except Exception as error:
            raise RuntimeError(f"there was aproblem in accessing student paid course details under login route:{error}")
        formated_details = [{"courseID":item[0],"courseName":item[1], "imageLink":item[2]} for item in details]
        allDetails = {
            "firstName":studentData[0],
            "lastName":studentData[1],
            "school":studentData[2],
            "intake":studentData[3],
            "courseDetails":formated_details

        }
        
        return jsonify(allDetails)
        

    
@app.route("/handleLiveSessionLinks", methods=["GET", "POST"])
def handleLiveSessionLinks():
    if request.method == "GET":
        try:
            courseDetails = session["courseDetails_loadedOnStudentPortal"]
            course_id = courseDetails["courseId"]
            cohort = courseDetails["cohort"]

            if course_id is None:
                # No course ID found in session
                return jsonify({"error": "Course ID not found in session"})
            with sqlite3.connect("liveSessionLinks.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    SELECT
                        link,
                        DateofliveClass,
                        SessionTime,
                        InstructorName,
                        Topic
                    FROM
                        liveSessions
                    WHERE
                        CourseId == ? and Cohort == ?
                    ORDER BY link DESC
                    LIMIT 1
                """,(course_id,cohort))
                data = cursor.fetchone()

            if data:
                # print(f" live link data:{data}")
                return jsonify({"link":data[0], "DateOfClass":data[1],"Time":data[2],"instructorName":data[3],"Topic":data[4]}) 
            else:
                return jsonify({"No Link": "There is no live session link for this course"})
        except sqlite3.Error as error:
            raise RuntimeError(f"Error occurred while accessing the liveSession link database:{error}")
        except Exception as error:
            raise RuntimeError(f"Error occurred while accessing the liveSession link database: {error}")

    
    elif request.method == "POST":
        # Handle POST requests
        pass
    
    # If the request method is neither GET nor POST, return an error response
    return jsonify({"error": "Unsupported request method on handle live link route"})





@app.route("/handleRecordedLinks", methods=["POST","GET"])
def handleRecordedLinks():

    
         
    # if request.method == "POST":
    #     pass
    #     data = request.json
    #     session["course_id_studentPorta"] = data["courseId"]
    #     # print("recieved it :",data)
    #     """ handle post requests from the admin dashboard ie populating the recorded table"""
    if  request.method == "GET":
        courseDetails = session["courseDetails_loadedOnStudentPortal"]
        course_id = courseDetails["courseId"]
        cohort = courseDetails["cohort"]

        with sqlite3.connect("liveSessionLinks.db") as db:
            cursor = db.cursor()
            cursor.execute("""
                SELECT
                    DateOfRecording,
                    Link,
                    SessionTitle,
                    TopicCovered,
                    CourseId
                FROM
                    recordedLinks
                WHERE
                    CourseId == ? AND Cohort==?
            """,(course_id,cohort))
            data = cursor.fetchall()
        if data:
            sortedData = [{"Date": item[0], "Link":item[1],"SessionTitle":item[2],"topicCovered":item[3]} for item in data]

            return jsonify(sortedData)
        else:
            return jsonify({"No Recordings":"session recording is not yet ready"})
    return jsonify({"error": "Unsupported request method on handle recorded link route"})

@app.route("/handleOnlinetests", methods=["GET","POST"])
def handleOnlineTests():
    studentId = current_user.id
    try:
        courseDetails = session["courseDetails_loadedOnStudentPortal"]
        courseId = courseDetails["courseId"]
        cohort = courseDetails["cohort"]
    except Exception as error:
            raise RuntimeError(f"session in handleonlineTest route failed {error}")
    if request.method == "GET":  
        if courseId:
            # print(courseId)
            with sqlite3.connect("testDataBase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    SELECT
                        q.TestId,q.CourseId,q.Question,q.Options
                    FROM
                        questionDetails AS q

                    WHERE
                        q.CourseId == ? AND CohortId == ?
                """, (courseId,cohort))
                data = cursor.fetchall()
            if data:
                print(f"cheek:{data}")
                formatedData = []
                for questionObject in data:
                    formatedData.append({
                        "studentId": studentId,
                        "TestId":questionObject[0],
                        "courseId": questionObject[1],                           
                        "Question":questionObject[2],
                        "Options": questionObject[3].split(",")
                    })
                # print(formatedData)

                return jsonify(formatedData)
            else:
                return jsonify({"Test Status":"No test yet"})
            
    else:
        Results = request.json
        try:
            testResults = TestStudentAnswes(Results)
            testResults.createTable()
            testResults.insertIntotable()
            if Results:
                """
                    making results after populating the student test answer  database
                """
                try:
                    student = AssessmentResults(studentId= studentId, courseId= courseId)
                    student.markResults()
                except Exception as e:
                    raise RuntimeError(e)
        except Exception as error:
            raise RuntimeError(f"error on dealing with student test respons:{error}")
        
    return jsonify({"api status":"handleOnlinetest api failure"})
""" retrive test questions from the data base and send them to client server
    access the course to retrive quesions for from the course if which is stored in the
    session under handlerecorded link route
"""

@app.route("/handleOnlineExams", methods=["GET","POST"])
def handleOnlineExams():

    studentId = current_user.id
    try:
        courseDetails = session["courseDetails_loadedOnStudentPortal"]
        courseId = courseDetails["courseId"]
        cohort = courseDetails["cohort"]
    except Exception as error:
        return f"session in handleonlineExam route failed {error}"
    
    if request.method == "GET":
        if courseId:
            with sqlite3.connect("examDataBase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    SELECT
                        q.ExamId,q.CourseId,q.Question,q.Options,q.Duration
                    FROM
                        questionDetails AS q

                    WHERE
                        q.CourseId == ? AND Cohort == ?
                """, (courseId, cohort))
                data = cursor.fetchall()
            if data:
                # print(data)
                formatedData = []
                for questionObject in data:
                    formatedData.append({
                        "studentId": studentId,
                        "ExamId":questionObject[0],
                        "courseId": questionObject[1],                           
                        "Question":questionObject[2],
                        "duration":questionObject[4],
                        "Options": questionObject[3].split(",")
                    })
                
                

                return jsonify(formatedData)
            else:
                return jsonify({"Exam Status":"No exam yet"})
            
    else:
        studentAnswers = request.json
        answer = ExamStudentAnswes(studentAnswers)
        answer.createTable()
        answer.insertIntoTable()

        """
            making results after populating the student exam answer  database
        """
        try:
            student = AssessmentResults(studentId= studentId, courseId= courseId)
            student.markResults()
        except Exception as e:
            raise RuntimeError(e)

    return jsonify({"api status":"handleOnlineExam api failure"})



@app.route("/loadPaidcourseOnstudentPortal", methods=["POST","GET"])
def loadPaidCourseONPortal():
    if request.method == "POST":
        requestType = request.json.get("type")
        if requestType == "student-paid-course":
            data = request.json.get("data")            
            session["courseId_loadedOnStudentPortal"] = data["courseId"]
            session["courseDetails_loadedOnStudentPortal"] = data


    return render_template("paidcourseOnportal.html")

@app.route("/handleCourseYouTubeLink", methods = ["GET","POST"])
def handleCourseYouTubeLink():
    if request.method == "GET":
        courseId = session.get("courseId_loadedOnStudentPortal")
        try:
            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    SELECT
                        youtubeLink 
                    FROM
                        courseYoutubeLink
                    WHERE
                        courseId == ?         
                """,(courseId,))
                data = cursor.fetchone()
            # print(f"youtube link:{data}")
            return jsonify({"link":data})
        except sqlite3.Error as error:
            return f"api failed to connect to courseDatabase in loadPaidcourseOnstudentPortal route: {error}"
        except Exception as error:
            return f"error face while accessing courseDatabase in loadPaidcourseOnstudentPortal:{error} "

    elif request.method == "POST":
        pass
    else:
        return {"api status":"api failed to fetch course youtube link"}
    


@app.route("/handleStudentscores", methods =["GET"])
def handleStudentscores():
    if request.method == "GET":
        studentMarks = []
        courseId = session.get("courseId_loadedOnStudentPortal")
        studentId = current_user.id
        if courseId and studentId:
            try:
                with sqlite3.connect("studentScoresDatabase.db") as db:
                    cursor = db.cursor()
                    cursor.execute("""
                        SELECT
                            s.Scores
                        FROM
                            testREsults AS s
                        WHERE
                            s.StudentId == ? and s.CourseId == ?     
                    """,(studentId, courseId))
                    data = cursor.fetchone()
                if data:
                    studentMarks.append({"test":data[0]})

            except sqlite3.Error as e:
                raise RuntimeError(f"sql connection error: {e}")
            except Exception as error:
                raise RuntimeError(f"Error while retriving student test scores {error}")
            
            try:
                with sqlite3.connect("studentScoresDatabase.db") as db:
                    cursor = db.cursor()
                    cursor.execute("""
                        SELECT
                            e.Scores
                        FROM
                            examResults AS e
                        WHERE
                            StudentId == ? AND CourseId == ?
                    """,(studentId, courseId))
                    data = cursor.fetchone()
                    if data:
                        studentMarks.append({"exam":data[0]})

            except sqlite3.Error as e:
                raise RuntimeError(f"sql connection error: {e}")
            except Exception as error:
                raise RuntimeError(f"Error while retriving student exam scores {error}")
            

            return jsonify(studentMarks)
                
        else:
            return jsonify({"student and course IDs":"not suplied"})
        
    else:
        pass
    return jsonify({"api status":" handleStudentResults api failed"})


@app.route("/studentProfile", methods=["GET", "POST"])
def studentProfile():
    if request.method == "GET":
        requestType = request.args.get("type")
        if requestType == "studentDetails":
            studentId = current_user.id
            try:
                student = FetchStudentData(studentId= studentId)
                studentData = student.studentBio()
                details = {"fName": studentData[0], "sName":studentData[1], "school":studentData[2],"cohort":studentData[3],"phone":studentData[4],"email":studentData[5]}
                return jsonify(details)
                
            except Exception as error:
                raise RuntimeError(f"error while initiating FetchStudentData class:{error}")


    return render_template("studentProfile.html")

@login_required
@app.route("/admin", methods =["GET"])
def admin():
    if not  current_user.is_authenticated:
        session["admin_referrer"] = request.url
        return redirect(url_for('adminLogin'))
    return render_template("adminDashoard.html")

@app.route("/adminDashboardStatistics", methods=["GET","POST"])
def adminDashboardStatistics():
    if request.method == "GET":
        requestBody = request.args.get("type")
        if requestBody == "numberofCourses":
            courseDetails = CourseDetailsApi()
            numberOfCourses = courseDetails.numberOfAvailableCourses()
            return jsonify(numberOfCourses)
        elif requestBody == "numberofstudents":
            students = StudentApi()
            numberOFstudents = students.numberOfStudents()
            return jsonify(numberOFstudents)
        elif requestBody == "numberOfSchools":
            school = SchoolApi()
            numberOfschool = school.numberOfSchools()
            return jsonify(numberOfschool)
            


    

@app.route("/adminSchoolPage")
def adminSchoolPage():
    return render_template("adminSchoolPage.html")

@app.route("/handleAdminSchoolPage", methods=["POST", "GET"])
def handleAdminSchoolPage():
    if request.method == "POST":
        data = request.data
        data = data.decode("utf-8")
        # print(data)
        formatedData = json.loads(data)
        s = formateSchoolData(formatedData)
        """ inserting school details to the school database """
        school = SchoolDatabes(s)
        created = school.createTables()
        inserted = school.insertIntotables()
        # print(created)
        # print(inserted)
        
        

    
    try:
        with sqlite3.connect("schoolsDatabase.db") as db:
            cursor = db.cursor()
            cursor.execute("""
                SELECT
                    S.SchoolId, 
                    S.SchoolName,
                    C.CoordinatorName,
                    U.Url
                FROM
                    schoolDetails AS S 
                JOIN
                    SchoolCoordinator AS C ON C.SchoolId == S.SchoolId
                JOIN
                    schoolUrl AS U ON  U.SchoolId == S.SchoolId

            """)
            data = cursor.fetchall()
        formatedData =  [{"schoolId":object[0], "schoolName":object[1], "url":object[3],"schoolCoordinator":object[2]} for object in data]
        # print(formatedData)
        return jsonify(formatedData)

    except sqlite3.Error as error:
        return f"faced sql connection error on fetching from school database:{error}"
    except Exception as error:
        return f"faced error on fetching from school database: {error}"
    

@app.route("/showAdminSchoolDetailsToDelete")
def showAdminSchoolDetailsToDelet():
    # url = url_for('showAdminSchoolDetailsToDelet')
    return render_template("schoolTodelet.html")

    
@app.route("/handleAdminSchoolDeletion", methods=["POST","GET"])
def handleAdminSchoolDeletion():
    if request.method == "POST":
        type_param = request.json.get("type")

        if type_param == "id":
            data = request.json.get("data")
            session["schoolId_to_delet"] = data
            # print(data)
        elif type_param == "delete":
            schoolTodelete = session.get("schoolId_to_delet")
            with sqlite3.connect("schoolsDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    DELETE FROM
                        schoolDetails
                    WHERE
                        SchoolId == ?
                               
                """,(schoolTodelete,))
                db.commit()

        
    elif request.method == "GET":
        type_args = request.args.get("type")
        # print(type_args)
        if type_args == "get_data":
            schoolId = session.get("schoolId_to_delet")
            # print(schoolId)
            if schoolId:
                with sqlite3.connect("schoolsDatabase.db") as db:
                    cursor = db.cursor()
                    cursor.execute("""
                        SELECT
                            S.SchoolId, 
                            S.SchoolName,
                            C.CoordinatorName
                        FROM
                            schoolDetails AS S 
                        JOIN
                            SchoolCoordinator AS C ON C.SchoolId == S.SchoolId
                        WHERE
                            S.SchoolId == ?  
                    """,(schoolId,))
                    data = cursor.fetchall()
                # print(data)
                return jsonify({"data":data[0]})

    return jsonify({"response":"success"}),200


"""
    To do list:   improve the code bellow
"""

@app.route("/adminschoolTemplate", methods = ["POST","GET"])
def adminschoolTemplate():
    if request.method == "POST":
        body = request.json.get("type")
        if body == "schoolId":
            id = request.json.get("id")
            # print(f"clicked on course {id}")
            session["schoolToLoad"] = id
            return jsonify({"status":"ok"})
        elif body == "addCourse":
            courseDetails = request.json.get("body")
            courseDetails = json.loads(courseDetails)

            if courseDetails:
                try:
                    courseId = courseDetails["cId"]
                    schoolId = courseDetails["sId"]
                    courseName = courseDetails["cName"]
                    coursePriceId = courseDetails["cPriceId"]
                    coursePrice = courseDetails["cPrice"]
                    discription = courseDetails["Dscrp"]
                    courseImageLink = courseDetails["imgLnk"]
                    youtubeLink = courseDetails["utubeLnk"]
                    courseDuration = courseDetails["cDuration"]
                    routeFunction = courseDetails["routeFunction"]
                    courseObj = {
                        "courseId":courseId,
                        "schoolId": schoolId,
                        "courseName": courseName,
                        "coursePriceId":coursePriceId,
                        "coursePrice":coursePrice,
                        "discription":discription,
                        "courseImageLink":courseImageLink,
                        "youtubeLink":youtubeLink,
                        "courseDuration":courseDuration,
                        "routeFunction":routeFunction
                    }
                    # print(courseObj)

                    db = Courses(courseObject= courseObj)

                    # create tables
                    db.createTables()
                    # insert into tables
                    db.insertIntoTables()
                except Exception as error:
                    raise RuntimeError(f"error whill populating course database:{error}")
            return jsonify({"requestStatus":"ok"}),200
    elif request.method == "GET":
        typeAgr = request.args.get("type")
        schoolId= session["schoolToLoad"]
        if schoolId:
            if typeAgr == "schoolName":
                try:
                    with sqlite3.connect("schoolsDatabase.db") as db:
                        cursor = db.cursor()
                        cursor.execute("""
                            SELECT
                                s.SchoolName
                            FROM
                                schoolDetails AS s
                            WHERE
                                s.SchoolId == ?     
                                
                        """,(schoolId,))
                        results1 = cursor.fetchone()
                    # print(results1[0])
                    return jsonify({
                        "name":results1[0]
                    })
                except sqlite3.Error as error:
                    raise RuntimeError(f"connection  error on retriving school details:{error}")
                except Exception as error:
                    raise RuntimeError(f"Error while retriving school details:{error}")
            elif typeAgr == "courseDdetails":
                try:
                    courseOb = CourseDetailsApi()
                    data = courseOb.fetchAvaibleCourses(schoolId=schoolId)
                    details = [{"courseId":course[0], "courseName":course[2]} for course in data]
                    return jsonify({"data":details})
                except Exception as error:
                    raise RuntimeError( f"faced error while dealing with Course details api in adminschoolTemplate route : {error}")

    return render_template("adminschoolTemplate.html")

@app.route("/courseTodelete",methods = ["GET","POST"])
def courseTodelete():
    if request.method == "POST":
        bodyType = request.json.get("type")
        if bodyType and bodyType == "DeletCourse":
            courseData = request.json.get("Details")
            courseData = json.loads(courseData)
            session["course_to_delete"] = courseData
            # print(courseData)
            return jsonify({"status":"ok"})
        elif bodyType and bodyType == "delete":
            data = request.json.get("body")
            if data and data == "yes":
                courseTodelete = session.get("course_to_delete")
                id = courseTodelete["courseID"]
                # print(courseTodelete["courseID"])
                try:
                    with sqlite3.connect("courseDatabase.db") as db:
                        cursor = db.cursor()
                        cursor.execute("""
                            DELETE FROM
                                courseDetails
                            WHERE
                                courseId == ? 
                        """,(id,))

                except sqlite3.Error as error:
                    print(f"Connection error course debase:{error}")
                    return f"Connection error course debase:{error}"
                except Exception as error:
                    print(f"error while accessing course debase:{error}")
                    return f"error while accessing course debase:{error}"

    return render_template("courseTodelete.html")


@app.route("/admincourseInterface", methods =["GET","POST"])
def admincourseInterface():
    if request.method == "POST":
        requestType = request.json.get("type")
        if requestType == "courseId":
            CourseId = request.json.get("body")
            # print(f" stored {CourseId}")
            if CourseId:
                session["adminAccessedCourse"] = CourseId
                return jsonify({"status":"course id recieved"})

            
        elif requestType == "linkDetails":
            data = request.json.get("data")
            if data:
                "live sesstion class call"
                live_sessionObject = LiveSessions()
                live_sessionObject.creatTables()
                linkType = data["linkType"]
                if linkType == "live":
                    "populate live session data base"
                    live_sessionObject.insertIntoliveSessionsTable(dataObject=data)
                    return jsonify({"status":"link data recieved"})
                elif linkType == "recorded":
                    "populate recorded session data base"
                    live_sessionObject.insertIntorecordedLinksTable(dataObject=data)
                    return jsonify({"status":"link data recieved"})
        elif requestType == "questions":
            data = request.json.get("data")
            if data:
                questionType = data["questionType"]
                if questionType == "exams":
                    """populate exam data base here"""
                    courseID = data["courseId"]
                    Examcohort = data["cohort"]
                    time = data["time"]
                    examQuestionObject = data["questionObject"]
                    examQuestionObject = json.loads(examQuestionObject)
                    # print(examQuestionObject)                   

                    paperIds = CreatePaperIds(courseId=courseID,cohort=Examcohort)
                    examID = paperIds.examId()
                    # print(examID)
                    # print(courseID)
                    # print(type(time))
                    # print(examQuestionObject)

                    exam = Exams(questionObject=examQuestionObject,courseId=courseID,examId=examID,cohort=Examcohort,duration=time)
                    exam.createTables()
                    exam.insertIntoTable()
                    
                else:
                    """populate test database here"""
                    _courseID = data["courseId"]
                    Testcohort = data["cohort"]
                    Testtime = data["time"]
                    questionObject = data["questionObject"]
                    questionObject = json.loads(questionObject)

                    paperIds = CreatePaperIds(courseId= _courseID, cohort=Testcohort)
                    testId = paperIds.testId()
                    # print(testId)

                    """teting the test class """
                    Testobj = Test(questionObject=questionObject ,courseId=_courseID,testId=testId,cohort=Testcohort,duration=Testtime)
                    Testobj.createTables()
                    Testobj.insertIntoTable()
                   
                return jsonify({"response Status":"question recieved"})

    else:
        getRequestType = request.args.get("type")
        if getRequestType == "courseDetails":
            courseId = session.get("adminAccessedCourse")
            if courseId:
                try:
                    with sqlite3.connect("courseDatabase.db") as db:
                        cursor = db.cursor()
                        cursor.execute("""
                            SELECT
                                C.courseName,D.courseDiscription
                            FROM
                                courseDetails AS C
                            JOIN
                                courseDiscription AS D ON D.courseId == C.courseId
                            WHERE
                                C.courseId == ?      
                        """,(courseId,))
                        data = cursor.fetchall()
                        formated = data[0]
                    return jsonify({"CourseName":formated[0],"CourseDEscription":formated[1],"courseId":courseId})

                except sqlite3.Error as error:
                    print(error)
                    return f"connection error while retriving course Details: {error}"
                except Exception as error:
                    print(error)
                    return f"error while retriving course Details: {error}"
            
        
    return render_template("admincourseInterface.html")


if __name__ == "__main__":
    app.run(debug=True)
    # socketio.run(app, debug=True)