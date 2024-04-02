

from flask import Flask, render_template,request,redirect, session,url_for,jsonify,flash
from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin,login_user,login_required,logout_user,current_user
from wtforms import SelectField,StringField,SubmitField,EmailField,PasswordField
from wtforms.validators import DataRequired
import pycountry
import os
import sqlite3
from databases import ExamStudentAnswes, Exams, Test,TestStudentAnswes,AssessmentResults, StudentDatabases, PurchasedCourseDetails, FetchStudentData, LiveSessions,ExamStudentAnswes, CoursePaymentsDataDase
from createStudentId import CreateStudentId
# from createPaymentRefrenceNumber import GenerateCoursePaymentRefrenceNumber
from authentication import GetStudent
from envKeys import strip_key,stripwhookkey,ALC_SECURITY
import stripe





app = Flask("__name__")
login_manager = LoginManager()
login_manager.init_app(app)

YOUR_DOMAIN = 'http://127.0.0.1:5000'
stripe.api_key = strip_key
# stripe.Product.create(name="database")
# stripe.Price.create(
#   product='{{PRODUCT_ID}}',
#   unit_amount=2000,
#   currency="usd",
# )

try:
    security = ALC_SECURITY
    app.config["SECRET_KEY"] = security

except ValueError as error:
    print(f"set App secrat key:{error} ")
except Exception as error:
    print(f"app secrat key is not set. in the termino type export{error} =  set your key here" )

def getCountries():
    return [(country.alpha_2, country.name)for country in pycountry.countries]
available_schools = [("datascience","School of Data Science"),("softwareEngineering", "School of Software Engineering")]
intake_list = [("January","January in-Take"),("Apirl","April in-Take"),("August","August in-Take")]


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
    intake = SelectField(label="Choose the in-take", choices=intake_list)
    submit = SubmitField(label= "Submit")

class StudentLoginForm(FlaskForm):
    studentId = StringField(label=" Your Student Id", validators=[DataRequired(message="It's a must")])
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
    type_of_partnernship = SelectField(label="Type of partnership",choices=[("grant","Grant Partner"),("corporate_ally","Corporate Ally")])
    purpose_of_partnership = StringField(label="Purpose of Financial Partnership ")
    expection_from_partnership = StringField(label="Expected Benefits or Returns from the Partnership (if any):")
    more_info = StringField(label="Is there anything else you would like us to know about your interest in a financial partnership with ALC? ")

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

""" creating tables for live and recorded sessions """

sessionClasses = LiveSessions()
sessionClasses.creatTables()
# note data this call is for demo, the insertintorecorded function should be Called 
# in the admin dashboard in the route where addmin enters recorded details
# # # therefore it should be removed from here after testing
# sessionClasses.insertIntorecordedLinksTable("https/24453dsd.com","12/12/2024","HTML CLASS","TagS","prod_PcWpcg8596849j")
# sessionClasses.insertIntoliveSessionsTable("23/23/2023","2:30pm - 3:30pm","prod_PcWpcg8596849j","https/er34t343.com","Dr Tom","mathematics of Ai")

"""
    demo  exam data
"""
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

# exam = Exams(questions,"prod_PcWpcg8596849j","dasci123")
# exam.createTables()
# exam.insertIntoTable()

"""teting the test class """
# Testobj = Test(testQuestions,"prod_PcWpcg8596849j","test019")
# Testobj.createTables()
# Testobj.insertIntoTable()



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

@app.route("/contact")
def contactPage():
    return render_template("contactPage.html")

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

@app.route("/projectpage")
def projectPage():

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
                        student = CreateStudentId(sirName= sirName)
                        studentId = student.makeStudentId()
                    except ValueError as error:
                        print(f" probably create student id class failed. check the error: {error}")
                    #create database 
                    studentDataBase = StudentDatabases(studentId= studentId ,firstname=fName,sirName=sName,gender=studentGender,phoneNumber=pnumber,email=emailAddress,school=schoolOfAttachment,password=studentPassword,intake=intakeChoosen,country=countryOfOrigin,)

                    """ creating tables """
                    studentDataBase.createTables()
                    """inserting values into the created tables"""
                    studentDataBase.insertIntoTables()
                    return redirect(url_for('login'))
                else:
                    return redirect(url_for('registrationPage'))
            except ValueError as error:
                print(f"possibly password did not match or student database wasnt properly created. check the error:{error}")
        else:
            print(f"the submit button on the form has issues: {form.errors}")
    except Exception as error:
        print(f"the register form structure call failed: {error}")
    
    return render_template("registrationPage.html",RegForm= form)


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
            firsNname = form.firstName.data
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
            flash(f"{firsNname,sirName,affriation}")
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
        print(f"the register form structure call failed: {error}")
    
    return render_template("partnerPage.html", form=form)


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
                """session bellow stores logged instudent id which is to be used getBioDataAndCourseDetails route """
                
                login_user(user=user)
                session["logged_student_id"] = current_user.id
                next_url = session.pop("payment_url", None)
                # if request.referrer and "/payments" in request.referrer:
                if next_url and "/payments" in next_url:

                    return redirect(url_for('payment'))
                else:
                    return redirect(url_for('studentDashboard'))
            return redirect(url_for('login'))
    except Exception as error:
        print(f"possibility that student login class didnt work:{error}")
    return render_template("studentLogin.html",form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('homePage'))

@login_required
@app.route("/studentDashboard", methods = ["POST","GET"])
def studentDashboard():
    
    return render_template("studentDashboard.html")


@app.route("/payments",methods=["POST","GET"])
def payment():
    if not current_user.is_authenticated:
        session["payment_url"] = request.url
        return redirect(url_for('login'))        
    try:
        priceId = session.get("fetched_course_pirce_details")
        # print(f"price details here:{courseDetails}")
        # id = courseDetails["priceId"]
        # amount = courseDetails["price"]
        # print(f"price id:{priceId}")
    
        session["current_student"] = current_user.id
        
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': priceId,
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/studentDashboard',
                cancel_url=YOUR_DOMAIN + '/login'
            )
        except Exception as e:
            return str(e)
    except Exception as error:
        print(f"course details not found in session:{error}")
        return jsonify({"course details not found in session"}),400
    
    # if request.method == "POST":
    #     payment_response  = request.data
    #     print(f"resonse from strip: {payment_response}")

    return redirect(checkout_session.url,code=303)



@app.route("/fetchCourseDetails",methods=["POST","GET"])
def fetchCourseDetails():
    try:
        if request.method == "POST":
            data = request.json
            # print(f"recieved data:{data}")
            course_id = data.get("send_courseId")
            if course_id:
                # print(f"course id captured from the front end:{course_id}")
                # Store course ID in session for later retrieval in GET request
                session["course_id"] = course_id
                return jsonify({"message": "Course ID received successfully"}), 200
            else:
                return jsonify({"error": "No course ID provided in the request"}), 400
        elif request.method == "GET":
            course_id = session.get("course_id")
            # print(f"course id retrived from the session:{course_id}")
            if course_id:
                try:
                    with sqlite3.connect("courseDatabase.db") as db:
                        cursor = db.cursor()
                        cursor.execute("""
                            select
                                c.courseId,p.coursePriceIds
                            FROM
                                courseDetails AS c
                            JOIN
                                coursePriceIdDetails AS P ON c.courseId == p.courseId
                            WHERE
                                c.courseId == ?
                        """,(course_id,))
                        course_details = cursor.fetchone()
                        if course_details:
                            courseId,priceId = course_details
                            # print(f"courseID id here:{courseId} \n")
                            session["fetched_course_pirce_details"] = priceId
                            current_student = session.get("current_student")
                            return jsonify({"studentId":current_student, "courseId":courseId, }),200
                        return jsonify({"error":"course not found"}),400

                except Exception as error:
                    print(f"failed to retrive data from course Database:{error}"),400
            else:
                return jsonify({"error":"no course id in the session"}),400
    except Exception as error:
        print(f"it is possible that server didnt recieve course id from the client server:{error}"),400



    

    
        
@app.route("/handlePayments")
def handlePayments():
    return render_template("continueToPayment.html")

@app.route("/studentPaidCourseRecords",methods=["GET","POST"])
def paymentRecieved():
    # this route updates the purchased course database when the payment is successfully made
    if request.method == "POST":
        data = request.json
        if data:
            student = data["studentId"]
            course = data["courseId"]
            paymentData = PurchasedCourseDetails(studentId= student, courseId= course)
            paymentData.createTables()
            paymentData.insertIntoTables()
    return render_template("continueToDashboard.html")



# Use this sample code to handle webhook events in your integration.
# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = stripwhookkey

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
        raise e
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        raise e

    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
      payment_intent = event['data']['object']
    # ... handle other event types
      print(f"response from strip:{payment_intent}")
    else:
      print('Unhandled event type {}'.format(event['type']))

    return jsonify(success=True)






@app.route("/getBioDataAndCourseDetails", methods= ["GET","POST"])
def getBioDataAndCourseDetails():
    if request.method == "GET":
        details = []
        """
            bellow we are accessing student bio data by initailizing student object then call studentBio function
        """
        studentId = session.get("logged_student_id")
                
        student  = FetchStudentData(studentId= studentId)
        studentData = student.studentBio()
        # print(f"fatched student data:{studentData}")
        try:
            """
                this api sends student bio data and course details on each login session which are to be rendered
                on student portal. so it sends those details to a js file which handle rendering 
                html content on student portal
            """
            with sqlite3.connect("purchasedCourseDetails.db") as db:
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
                        print(f"error in accessing course database in login route:{error}")
                # print(details)
                
                
        except sqlite3.Error as error:
            print(f"failed to connect to sqlite in the login route:{error}")
        except Exception as error:
            print(f"there was aproblem in accessing student paid course details under login route:{error}")
        formated_details = [{"courseID":item[0],"courseName":item[1], "imageLink":item[2]} for item in details]
        allDetails = {
            "firstName":studentData[0],
            "lastName":studentData[1],
            "school":studentData[2],
            "intake":studentData[3],
            "courseDetails":formated_details

        }
        # print(f" sent data: {allDetails}")
        
        return jsonify(allDetails)
        # elif request.method == "POST":
        #     return "handle post request "
    # return render_template("continueToDashboard.html")

    
@app.route("/handleLiveSessionLinks", methods=["GET", "POST"])
def handleLiveSessionLinks():
    if request.method == "GET":
        try:
            course_id = session.get("course_id_studentPortal")
            if course_id is None:
                # No course ID found in session
                return jsonify({"error": "Course ID not found in session"})
            # print(f"itttt:{course_id}")
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
                        CourseId == ?
                    ORDER BY link DESC
                    LIMIT 1
                """,(course_id,))
                data = cursor.fetchone()

            if data:
                # print(f" live link data:{data}")
                return jsonify({"link":data[0], "DateOfClass":data[1],"Time":data[2],"instructorName":data[3],"Topic":data[4]}) 
            else:
                return jsonify({"No Link": "There is no live session link for this course"})
        except sqlite3.Error as error:
            print(f"Error occurred while accessing the liveSession link database:{error}")
            return jsonify({"error": "Database error"})
        except Exception as error:
            print(f"Error occurred while accessing the liveSession link database: {error}")
            return jsonify({"error": "An unexpected error occurred"})
    
    elif request.method == "POST":
        # Handle POST requests
        pass
    
    # If the request method is neither GET nor POST, return an error response
    return jsonify({"error": "Unsupported request method on handle live link route"})


@app.route("/recieveLoadedCourseIdOnStudentPortal", methods= ["post"])
def recieveLoadedCourseIdOnStudentPortal():
    try:
        if request.method == "POST":
            data = request.json
            
            session["course_id_studentPortal"] = data["courseId"]
            # print(f"the real one :{data}")
    except Exception as error:
        return f"api failed to fecth course i on the student portal :{error}"
    return jsonify({"api satus":"recieveLoadedCourseIdOnStudentPortal failed"})


@app.route("/handleRecordedLinks", methods=["POST","GET"])
def handleRecordedLinks():
        
        
    if request.method == "POST":
        pass
        # data = request.json
        # session["course_id_studentPortal"] = data["courseId"]
        # print("recieved it :",data)
        """ handle post requests from the admin dashboard ie populating the recorded table"""
    elif  request.method == "GET":
        course_id = session.get("course_id_studentPortal")
        # print(f"check this id:{course_id}")
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
                    CourseId == ?
            """,(course_id ,))
            data = cursor.fetchall()
            # print(f"check this out:{data}")
        if data:
            sortedData = [{"Date": item[0], "Link":item[1],"SessionTitle":item[2],"topicCovered":item[3]} for item in data]

            return jsonify(sortedData)
        else:
            return jsonify({"No Recordings":"session recording is not yet ready"})
    return jsonify({"error": "Unsupported request method on handle recorded link route"})

@app.route("/handleOnlinetests", methods=["GET","POST"])
def handleOnlineTests():
    if request.method == "GET":
        studentId = session.get("logged_student_id")
        # print(f"student to do the paper:{studentId}")
        try:
            courseId = session.get("course_id_studentPortal")
            # print(f"cid:{courseId}")
            if courseId:
                with sqlite3.connect("testDataBase.db") as db:
                    cursor = db.cursor()
                    cursor.execute("""
                        SELECT
                            q.TestId,q.CourseId,q.Question,o.Options
                        FROM
                            questionDetails AS q
                        JOIN
                            options AS o ON o.CourseId == q.CourseId AND o.TestId == q.TestId
    
                        WHERE
                            q.CourseId == ?
                    """, (courseId,))
                    data = cursor.fetchall()
                if data:
                    # print(data)
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

        except Exception as error:
            return f"session in handleonlineTest route failed {error}"
    else:
        Results = request.json
        # print(f"test answers :{tresults}")
        testResults = TestStudentAnswes(Results)
        testResults.createTable()
        testResults.insertIntotable()
    return jsonify({"api status":"handleOnlineExam api failure"})
    """ retrive test questions from the data base and send them to client server
        access the course to retrive quesions for from the course if which is stored in the
        session under handlerecorded link route
    """

@app.route("/handleOnlineExams", methods=["GET","POST"])
def handleOnlineExams():
    if request.method == "GET":
        studentId = session.get("logged_student_id")
        # print(f"student to do the paper:{studentId}")
        try:
            courseId = session.get("course_id_studentPortal")
            # print(f"cid:{courseId}")
            if courseId:
                with sqlite3.connect("examDataBase.db") as db:
                    cursor = db.cursor()
                    cursor.execute("""
                        SELECT
                            q.ExamId,q.CourseId,q.Question,o.Options
                        FROM
                            questionDetails AS q
                        JOIN
                            options AS o ON o.CourseId == q.CourseId AND o.ExamId == q.ExamId
    
                        WHERE
                            q.CourseId == ?
                    """, (courseId,))
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
                            "Options": questionObject[3].split(",")
                        })
                    # print(formatedData)

                    return jsonify(formatedData)
                else:
                    return jsonify({"Exam Status":"No exam yet"})

        except Exception as error:
            return f"session in handleonlineExam route failed {error}"
    else:
        studentAnswers = request.json
        answer = ExamStudentAnswes(studentAnswers)
        answer.createTable()
        answer.insertIntoTable()

        # print(studentAnswers)
    return jsonify({"api status":"handleOnlineExam api failure"})



@app.route("/loadPaidcourseOnstudentPortal")
def loadPaidCourseONPortal():

    return render_template("paidcourseOnportal.html")

@app.route("/handleCourseYouTubeLink", methods = ["GET","POST"])
def handleCourseYouTubeLink():
    if request.method == "GET":
        courseId = session.get("course_id_studentPortal")
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
            print(f"youtube link:{data}")
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
        courseId = session.get("course_id_studentPortal")
        studentId = session.get("logged_student_id")
        # compiledResults= {}
        if courseId and studentId:
            # print(f"sid:{studentId} and cis:{courseId}")
            try:
                student = AssessmentResults(studentId= studentId, courseId= courseId)
                # student.formateStudentAnswerData()
                results = student.markResults()

                
                return jsonify(results)
            except Exception as error:
                return f"Error in handleStudentResults route{error}"
        else:
            return jsonify({"student and course IDs":"not suplied"})
        
    else:
        pass
    return jsonify({"api status":" handleStudentResults api failed"})


@app.route("/studentProfile")
def studentProfile():

    return render_template("studentProfile.html")



if __name__ == "__main__":
    app.run(debug=True)
    # socketio.run(app, debug=True)