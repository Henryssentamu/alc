
from ast import Raise
import json
import sqlite3
class StudentDatabases:
    def __init__(self, studentId, firstname,sirName, gender,phoneNumber,email, school,country,password, intake) -> None:
        self.studentId = studentId
        self.firstName = firstname
        self.sirname = sirName
        self.gender = gender
        self.phonenumber = phoneNumber
        self.email= email
        self.school = school
        self.country = country
        self.password = password
        self.intake = intake
    def createTables(self):
        """ note that in the school table, adjustment will be required
        ie instead of school name, insert school id from schools db"""
        try:
            with sqlite3.connect("StudentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS studentDetails(
                            Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            StudentId VARCHAR(50) PRIMARY KEY,
                            FirstName VARCHAR(30),
                            SirName VARCHAR(30)
                    )
                """)
            with sqlite3.connect("StudentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS studentGender(
                            Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            genderId INTEGER PRIMARY KEY AUTOINCREMENT,
                            Gender VARCHAR(50),
                            studentId VARCHAR(50),
                            FOREIGN KEY (studentId) REFERENCES studentDetails(StudentId)
                    )
                """)
            with sqlite3.connect("StudentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS studentContacts(
                            Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            contactId INTEGER PRIMARY KEY AUTOINCREMENT,
                            phoneNUmber VARCHAR(20),
                            email VARCHAR(50),
                            studentId VARCHAR(50),
                            FOREIGN KEY(studentId) REFERENCES studentDetails(StudentId)
                    )
                """)
            with sqlite3.connect("StudentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS studentCountryOfOrigin(
                            Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            studentCountryId INTEGER PRIMARY KEY AUTOINCREMENT,
                            CountryName VARCHAR(50),
                            studentId VARCHAR(50),
                            FOREIGN KEY (studentId) REFERENCES studentDetails(StudentId)
                    )
                """)
            with sqlite3.connect("StudentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS studentPasswords(
                            Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            PasswordId INTEGER PRIMARY KEY AUTOINCREMENT,
                            Password VARCHAR(50),
                            studentId VARCHAR(50),
                            FOREIGN KEY (studentId) REFERENCES studentDetails(StudentId)
                    )
                """)
            with sqlite3.connect("StudentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS studentSchools(
                            Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            school VARCHAR(50),
                            studentId VARCHAR(50),
                            FOREIGN KEY (studentId) REFERENCES studentDetails(StudentId)
                    )
                """)
            with sqlite3.connect("StudentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS studentIntake(
                            Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            Intake VARCHAR(20),
                            studentId VARCHAR(50),
                            FOREIGN KEY (StudentId) REFERENCES studentDetails(StudentId)
                            
                    )
                """)
        except sqlite3.Error as error:
            print(f" database connection error:{error}")
        except Exception as error:
            print(f" investigate this database error:{error}")
    def insertIntoTables(self):
        try:
            with sqlite3.connect("StudentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO studentDetails(
                            StudentId,
                            FirstName ,
                            SirName
                    ) VALUES(?,?,?)
                """,(self.studentId,self.firstName, self.sirname))
                db.commit()
            with sqlite3.connect("StudentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO studentGender(
                            Gender,
                            studentId
                    ) VALUES (?,?)
                """,(self.gender,self.studentId))
                db.commit()
            
            with sqlite3.connect("StudentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO studentContacts(
                            phoneNUmber,
                            email,
                            studentId
                    ) VALUES (?,?,?)
                """,(self.phonenumber, self.email, self.studentId))
                db.commit()
            
            with sqlite3.connect("StudentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO studentCountryOfOrigin(
                            CountryName,
                            studentId
                    ) VALUES (?,?)
                """,(self.country, self.studentId))
                db.commit()
            with sqlite3.connect("StudentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO studentPasswords(
                            Password,
                            studentId
                    ) VALUES (?,?)
                """,(self.password,self.studentId))
                db.commit()
            with sqlite3.connect("StudentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO studentSchools(
                            school,
                            studentId
                    ) VALUES (?,?)
                """,(self.school,self.studentId))
            with sqlite3.connect("StudentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO studentIntake(
                            Intake,
                            studentId
                    ) VALUES (?,?)
                """,(self.intake,self.studentId))
        except sqlite3.Error as error:
            print(f"faced database connection error:{error}")
        except Exception as error:
            print(f"investigate this database error:{error} ")

    

    


class CoursePaymentsDataDase:
    def __init__(self,studentId,studentName,phoneNumber,email, refrenceNumber) -> None:
        self.studentId = studentId
        self.studentName = studentName
        self.refrenceNumber = refrenceNumber
        self.phoneNumber = phoneNumber
        self.email = email
    def createTables(self):
        try:
            with sqlite3.connect("coursePaymentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS studentPaymentDetails(
                    Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    StudentId VARCHAR(50),
                    StudentFullName VARCHAR(60)
                    )
                """)
            with sqlite3.connect("coursePaymentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS paymentReferenceNumber(
                    Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    ReferenceNumber VARCHAR(200) PRIMARY KEY,
                    StudentId VARCHAR(50),
                    FOREIGN KEY (StudentId) REFERENCES studentPaymentDetails(StudentId)
                    )
                """)
            with sqlite3.connect("coursePaymentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS phoneNumberOnPayment(
                            Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            StudentId VARCHAR(50),
                            phoneNumber VARCHAR(50),
                            FOREIGN KEY(StudentId) REFERENCES  studentPaymentDetails(studentPaymentDetails) 
                    )

                """)
            with sqlite3.connect("coursePaymentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS emailsOnPayment(
                            Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            StudentId VARCHAR(50),
                            Email VARCHAR(200),
                            FOREIGN KEY(StudentId) REFERENCES studentPaymentDetails(StudentId)
                    )
                """)
        except sqlite3.Error as error:
            print(f"check out this error:{error}")
    def insertIntoTables(self):
        try:
            with sqlite3.connect("coursePaymentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO studentPaymentDetails(
                            StudentId,
                            StudentFullName
                    ) VALUES (?,?)
                """,(self.studentId, self.studentName))
            with sqlite3.connect("coursePaymentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO paymentReferenceNumber(
                            ReferenceNumber,
                            StudentId
                    ) VALUES(?,?)
                """, (self.refrenceNumber,self.studentId))
            with sqlite3.connect("coursePaymentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO phoneNumberOnPayment(
                            StudentId,
                            phoneNumber
                    ) VALUES (?,?)
                """,(self.studentId, self.phoneNumber))

            with sqlite3.connect("coursePaymentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO emailsOnPayment(
                            StudentId,
                            Email
                    ) VALUES(?,?)
                """,(self.studentId,self.email))
        except sqlite3.Error as error:
            print(f"investigate this table mentioned here: {error}")


class Courses:
    def __init__(self, courseObject) -> None:
        self.courseObject = courseObject
        
    def createTables(self):
        try:

            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS courseDetails(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        courseId TEXT PRIMARY KEY,
                        schoolId VARCHAR(300),
                        courseName VARCHAR(200)
                    )
                """)

                # cursor.execute("""
                #     CREATE TABLE IF NOT EXISTS CourseSchoolIdentity(
                #         Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                #         courseId TEXT,
                #         SchoolId VARCHAR(300),
                #         FOREIGN KEY(courseId) REFERENCES courseDetails(courseId) ON DELETE CASCADE
                #     )
                # """)
            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS coursePriceIdDetails(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        coursePriceIds TEXT PRIMARY KEY,
                        courseId TEXT,
                        coursePrice INTEGER,
                        FOREIGN KEY (courseId) REFERENCES courseDetails(courseId)  ON DELETE CASCADE 
                    )
                """)

            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS courseImageLinks(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        courseImageLink TEXT,
                        courseId TEXT,
                        FOREIGN KEY(courseId) REFERENCES courseDetails(courseId) ON DELETE CASCADE
                    )
                """)
            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS courseDiscription(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        courseId TEXT,
                        courseDiscription TEXT,
                        FOREIGN KEY(courseId) REFERENCES courseDetails(courseId) ON  DELETE CASCADE
                    )
                """)

            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS courseYoutubeLink(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        courseId TEXT,
                        youtubeLink TEXT,
                        FOREIGN KEY(courseId) REFERENCES courseDetails(courseId) ON DELETE CASCADE
                              
                    )
                """)
        except Exception as error:
            # print(f"somthing happened in creating course detail database: {error}")
            return f"somthing happened in creating course detail database: {error}"
    def insertIntoTables(self):
        try:
            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO courseDetails(
                        courseID,
                        schoolId,
                        courseName
                    ) VALUES(?,?,?)
                """,(self.courseObject["courseId"], self.courseObject["schoolId"], self.courseObject["courseName"]))
                # cursor.execute("""
                #     INSERT INTO CourseSchoolIdentity(
                #         courseId,
                #         SchoolId
                #     ) VALUES(?,?)
                # """,(self.courseObject["courseId"],self.courseObject["schoolId"]))
                db.commit()
            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO coursePriceIdDetails(
                        coursePriceIds,
                        courseId,
                        coursePrice  
                    )  VALUES(?,?,?)
                """,(self.courseObject["coursePriceId"],self.courseObject["courseId"],self.courseObject["coursePrice"]))
                db.commit()
            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO courseImageLinks(
                        courseImageLink,
                        courseId 
                    ) VALUES(?,?)
                """,(self.courseObject["courseImageLink"], self.courseObject["courseId"]))
                db.commit()
            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO courseDiscription(
                        courseId,
                        courseDiscription
                    ) VALUES(?,?)
                """,(self.courseObject["courseId"],self.courseObject["discription"]))
                db.commit()

            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO courseYoutubeLink(
                        courseId,
                        youtubeLink         
                    ) VALUES(?,?)
                """,(self.courseObject["courseId"],self.courseObject["youtubeLink"]))
                db.commit()
        except Exception as error:
            # print(f"faced chalenge in inserting data into course details. {error}")
            return f"faced chalenge in inserting data into course details. {error}"


class PurchasedCourseDetails:
    def __init__(self,studentId, courseId) -> None:
        self.studentId = studentId
        self.courseId = courseId
    def createTables(self):
        try:
            with sqlite3.connect("purchasedCourseDetails.db") as db:
                cursur = db.cursor()
                cursur.execute("""
                    CREATE TABLE IF NOT EXISTS studentDetails(
                            Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            PurchaseId INTEGER PRIMARY KEY AUTOINCREMENT,
                            StudentId VARCHAR(300)
                    )
                """)
            with sqlite3.connect("purchasedCourseDetails.db") as db:
                cursur = db.cursor()
                cursur.execute("""
                    CREATE TABLE IF NOT EXISTS purchasedCourse(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        CourseId TEXT,
                        StudentId VARCHAR(300),
                        FOREIGN KEY (StudentId) REFERENCES studentDetails(StudentId)
                    )
                """)
        except sqlite3.Error as e:
            print(f"failed to connect to sqlite:{e}")
        except Exception as error:
            print(f"possibility of failure to create specified table:{error}")

    def insertIntoTables(self):
        try:
            with sqlite3.connect("purchasedCourseDetails.db") as db:
                cursur = db.cursor()
                cursur.execute("""
                    INSERT INTO studentDetails(
                        StudentId    
                    ) VALUES(?)
                """, (self.studentId,))
                db.commit()

            with sqlite3.connect("purchasedCourseDetails.db") as db:
                cursur = db.cursor()
                cursur.execute("""
                    INSERT INTO purchasedCourse(
                        CourseId,
                        StudentId      
                    ) VALUES (?,?)
                """,(self.courseId,self.studentId))
                db.commit()
        except sqlite3.Error as e:
            print(f" error occured while insert in the purchasedCourseDetails :{e}")
        except Exception as error:
            print(f"possibility of failling to populate the specifed table:{error}")

        
class FetchStudentData:
    def __init__(self, studentId) -> None:
        self.studentId = studentId
    def studentBio(self):
        if self.studentId:
            try:
                with sqlite3.connect("StudentDetails.db") as db:
                    cursor = db.cursor()
                    # for any select update made here, there should be a corresponding  update in login route
                    cursor.execute("""
                        SELECT
                            S.FirstName,
                            S.SirName,
                            X.school,
                            I.Intake
                        FROM 
                            studentDetails AS S
                        JOIN
                            studentSchools AS X ON X.studentId == S.studentId
                        JOIN
                            studentIntake AS I ON I.studentId == S.studentId
                        WHERE
                            S.studentId == ?
                                   
                    """,(self.studentId,))
                    student_details = cursor.fetchone()
                    
            except sqlite3.Error as error:
                print(f"sqlite under fetch student details in stdent details class failed:{error}")
                return None
            except Exception as error:
                print(f"faced problames in fetching student details under student details class:{error}")
                return None
            return student_details
        else:
            return "either you did't provide student id or you provided empty one"

class LiveSessions:
    def __init__(self) -> None:
        pass
    def creatTables(self):
        try:
            with sqlite3.connect("liveSessionLinks.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS liveSessions(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        linkId INTEGER PRIMARY KEY AUTOINCREMENT,
                        DateofliveClass VARCHAR(200),
                        SessionTime VARCHAR(300),
                        CourseId TEXT,
                        link TEXT,
                        InstructorName VARCHAR(200),
                        Topic TEXT,
                        Cohort VARCHAR(200)       
                    )
                """)
            with sqlite3.connect("liveSessionLinks.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS recordedLinks(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        LinkId  INTEGER PRIMARY KEY AUTOINCREMENT,
                        DateOfRecording VAR(150),
                        Link TEXT,
                        SessionTitle TEXT,
                        TopicCovered TEXT,
                        CourseId TEXT,
                        Cohort VARCHAR(200)
                    )
                """)
        except sqlite3.Error as error:
            print(f"connection error:{error}")
        except Exception as error:
            print(f"error occured in creating liveseesion database:{error}")
    def insertIntoliveSessionsTable(self, dataObject):
        link =  dataObject["link"]
        SessionTime = dataObject["sessionTime"]
        CourseID = dataObject["courseId"]
        InstructorName = dataObject["instructor"]
        Topic = dataObject["topic"]
        cohort = dataObject["cohort"]
        Date = dataObject["date"]
        try:
            with sqlite3.connect("liveSessionLinks.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO liveSessions(
                        DateofliveClass,
                        SessionTime,
                        CourseId,
                        link,
                        InstructorName,
                        Topic,
                        Cohort
                               
                    ) VALUES (?,?,?,?,?,?,?)
                """,(Date,SessionTime,CourseID,link, InstructorName,Topic,cohort))
                db.commit()
        except sqlite3.Error as error:
            print(f" faced error while inserting into live link table:{error}")
        except Exception as error:
            print(f"error occured while insert into liveSessions table :{error}")


    def insertIntorecordedLinksTable(self,dataObject):
        link =  dataObject["link"]
        CourseId = dataObject["courseId"]
        SessionTitle = dataObject["topic"]
        TopicCovered = dataObject["topic"]
        cohort = dataObject["cohort"]
        DateOfRecording = dataObject["date"]
        try:
            with sqlite3.connect("liveSessionLinks.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO recordedLinks(
                        DateOfRecording,
                        Link,
                        SessionTitle,
                        TopicCovered,
                        CourseId,
                        Cohort
                    ) VALUES (?,?,?,?,?,?)
                """,(DateOfRecording,link,SessionTitle,TopicCovered,CourseId,cohort))
                db.commit()
        except sqlite3.Error as error:
            print(f"faced error while inserting into recorded link table:{error}")
        except Exception as error:
            print(f"error occured while inserting into liveSessions table :{error}")



class Exams:
    def __init__(self, questionObject,courseId, examId, cohort,duration) -> None:
        self.questionObject =  questionObject
        self.courseId = courseId
        self.examId = examId
        self.duration = duration
        self.cohort = cohort
        print(type(self.questionObject ))
        
    def createTables(self):
        try:
            with sqlite3.connect("examDataBase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS questionDetails(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        QuestionsId INTEGER PRIMARY KEY AUTOINCREMENT,
                        ExamId VARCHAR(200),
                        CourseId TEXT,
                        Question TEXT,
                        Cohort VARCHAR(500),
                        Duration VARCHAR(300)      
                    )
                        
                """)

            with sqlite3.connect("examDataBase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS options(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        OptionId INTEGER PRIMARY KEY AUTOINCREMENT,
                        CourseId TEXT,
                        ExamId TEXT,
                        Options TEXT,
                        FOREIGN KEY(CourseId) REFERENCES questionDetails(CourseId),
                        FOREIGN KEY(ExamId) REFERENCES questionDetails(ExamId) 
                    )
                        
                """)

            with sqlite3.connect("examDataBase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS answer(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        AnswerId INTEGER PRIMARY KEY AUTOINCREMENT,
                        CourseId TEXT,
                        ExamId TEXT,
                        Answer TEXT,
                        FOREIGN KEY(CourseId) REFERENCES questionDetails(CourseId),
                        FOREIGN KEY(ExamId) REFERENCES questionDetails(ExamId)  
                    )
                        
                """)
        except sqlite3.Error as error:
            print(f"failed to connect to exam database:{error}")
            return f"failed to connect to exam database:{error}"
        except Exception as error:
            print(f"exam data base error:{error}")
            return f"exam data base error:{error}"
    
    def insertIntoTable(self):
        
        for object in self.questionObject:
            # print("e",object)
            try:
                with sqlite3.connect("examDataBase.db") as db:
                    cursor = db.cursor()
                    cursor.execute("""
                        INSERT INTO  questionDetails(
                            ExamId,
                            CourseId,
                            Question,
                            Cohort,
                            Duration         
                        ) VALUES (?,?,?,?,?)
                            
                    """,(self.examId,self.courseId, object["question"],self.cohort,self.duration))
                    StringOptions = ",".join(object["options"])
                    cursor.execute("""
                        INSERT INTO  options(
                            CourseId,
                            ExamId,
                            Options         
                        ) VALUES (?,?,?)
                            
                    """,(self.courseId, self.examId, StringOptions))
                    
                    cursor.execute("""
                        INSERT INTO  answer(
                            CourseId,
                            ExamId,
                            Answer        
                        ) VALUES (?,?,?)
                            
                    """,(self.courseId, self.examId, object["correct_answer"]))
                    db.commit()
                
            except sqlite3.Error as error:
                print(f"Error On inserting into Exam databese :{error}")
                return f"Error On inserting into Exam databese :{error}"
            except Exception as error:
                print(f"Error On inserting into Exam databese :{error}")
                return f"Error On inserting into Exam databese :{error}"
            

class ExamStudentAnswes:
    def __init__(self, answerObject) -> None:
        self.answerObject = answerObject
    def createTable(self):
        try:
            with sqlite3.connect("studentExamAnswers.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS studentDetails(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        ResponseId INTEGER PRIMARY KEY AUTOINCREMENT,
                        StudentId VARCHAR(200)
                               
                    )
                """)
            with sqlite3.connect("studentExamAnswers.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS ExamDetails(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        ResponseId INTEGER PRIMARY KEY AUTOINCREMENT,
                        StudentId VARCHAR(200),
                        courseID TEXT,
                        ExamId VARCHAR(200),
                        FOREIGN KEY(StudentId) REFERENCES studentDetails(StudentId)
                               
                    )
                """)
            with sqlite3.connect("studentExamAnswers.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Answers(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        ResponseId INTEGER PRIMARY KEY AUTOINCREMENT,
                        StudentId VARCHAR(200),
                        courseID TEXT,
                        ExamId VARCHAR(200),
                        Answers TEXT,
                        FOREIGN KEY(StudentId) REFERENCES studentDetails(StudentId),
                        FOREIGN KEY(ExamId) REFERENCES  ExamDetails(ExamId),
                        FOREIGN KEY(courseID) REFERENCES  ExamDetails(courseID)
                                    
                    )
                """)
        except sqlite3.Error as error:
            return f"failed to connect to  studentExamAnswers.db:{error}"
        except Exception as error:
            return f"This error is related to studentExamAnswers database:{error} "
    def insertIntoTable(self):
        print(f"exa:{self.answerObject}")
        try:
            with sqlite3.connect("studentExamAnswers.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO studentDetails(
                        StudentId    
                    ) VALUES (?)
                """,(self.answerObject["studentId"],))
                db.commit()
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO ExamDetails(
                        StudentId,
                        courseID,
                        ExamId   
                    ) VALUES (?,?,?)
                """,(self.answerObject["studentId"],self.answerObject["courseId"],self.answerObject["ExamId"]))
                db.commit()
                stringedAnswerObject = ",".join(self.answerObject["answers"])
                # print(f" cytu:{stringedAnswerObject}")

                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO Answers(
                        StudentId,
                        courseID,
                        ExamId,
                        Answers  
                    ) VALUES (?,?,?,?)
                """,(self.answerObject["studentId"],self.answerObject["courseId"],self.answerObject["ExamId"],stringedAnswerObject))
                db.commit()
        except sqlite3.Error as error:
            return f"failed to connect to  studentExamAnswers.db:{error}"
        except Exception as error:
            return f"This error is related to studentExamAnswers database:{error} "



class Test:
    def __init__(self, questionObject,courseId, testId, cohort,duration) -> None:
        self.questionObject = questionObject
        self.courseId = courseId
        self.testId = testId
        self.cohort = cohort
        self.duration = duration
    def createTables(self):
        try:
            with sqlite3.connect("testDataBase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS questionDetails(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        QuestionsId INTEGER PRIMARY KEY AUTOINCREMENT,
                        TestId VARCHAR(200),
                        CourseId TEXT,
                        Question TEXT,
                        CohortId TEXT,
                        Duration VARCHAR(300)    
                    )
                        
                """)

            with sqlite3.connect("testDataBase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS options(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        OptionId INTEGER PRIMARY KEY AUTOINCREMENT,
                        CourseId TEXT,
                        TestId TEXT,
                        Options TEXT,
                        FOREIGN KEY(CourseId) REFERENCES questionDetails(CourseId),
                        FOREIGN KEY(TestId) REFERENCES questionDetails(TestId) 
                    )
                        
                """)

            with sqlite3.connect("testDataBase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS answer(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        AnswerId INTEGER PRIMARY KEY AUTOINCREMENT,
                        CourseId TEXT,
                        TestId TEXT,
                        Answer TEXT,
                        FOREIGN KEY(CourseId) REFERENCES questionDetails(CourseId),
                        FOREIGN KEY(TestId) REFERENCES questionDetails(TestId)  
                    )
                        
                """)
        except sqlite3.Error as error:
            # print(f"failed to connect to test database:{error}")
            return f"failed to connect to test database:{error}"
        except Exception as error:
            # print(f"test data base error:{error}")
            return f"test data base error:{error}"
    
    def insertIntoTable(self):
        
        for object in self.questionObject:
            try:
                with sqlite3.connect("testDataBase.db") as db:
                    cursor = db.cursor()
                    cursor.execute("""
                        INSERT INTO  questionDetails(
                            TestId,
                            CourseId,
                            Question,
                            CohortId,
                            Duration       
                        ) VALUES (?,?,?,?,?)
                            
                    """,(self.testId,self.courseId, object["question"],self.cohort, self.duration))
                    StringOptions = ",".join(object["options"])
                    cursor.execute("""
                        INSERT INTO  options(
                            CourseId,
                            TestId,
                            Options         
                        ) VALUES (?,?,?)
                            
                    """,(self.courseId, self.testId, StringOptions))
                    
                    cursor.execute("""
                        INSERT INTO  answer(
                            CourseId,
                            TestId,
                            Answer        
                        ) VALUES (?,?,?)
                            
                    """,(self.courseId, self.testId, object["correct_answer"]))
                    db.commit()
                
            except sqlite3.Error as error:
                # print(f"Error On inserting into test databese :{error}")
                return f"Error On inserting into test databese :{error}"
            except Exception as error:
                # print(f"Error On inserting into test databese :{error}")
                return f"Error On inserting into test databese :{error}"
            

class TestStudentAnswes:
    def __init__(self, answerObject):
        self.answerObject = answerObject
    def createTable(self):
        try:
            with sqlite3.connect("testanswers.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS studentdetails(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        Responses INTEGER PRIMARY KEY AUTOINCREMENT,
                        Studentid VARCHAR(200)    
                    )
                """)

            with sqlite3.connect("testanswers.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS courseDetails(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        Responses INTEGER PRIMARY KEY AUTOINCREMENT,
                        Studentid VARCHAR(200),
                        CourseId TEXT,
                        FOREIGN KEY(Studentid) REFERENCES studentdetails(Studentid) 
                    )
                """)

            with sqlite3.connect("testanswers.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS testDetails(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        Responses INTEGER PRIMARY KEY AUTOINCREMENT,
                        CourseId TEXT,
                        TestId VARCHAR(300),
                        FOREIGN KEY (CourseId) REFERENCES courseDetails(CourseId)
                    )
                """)

            with sqlite3.connect("testanswers.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS answers(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        Responses INTEGER PRIMARY KEY AUTOINCREMENT,
                        TestId VARCHAR(300),
                        Answers TEXT,
                        FOREIGN KEY (TestId) REFERENCES testDetails(TestId)
                    )
                """)

        except sqlite3.Error as error:
            return f"failed to connect to testAnswer db :{error}"
        except Exception as error:
            return f"error on test Answer db: {error}"
    def insertIntotable(self):
        try:
            with sqlite3.connect("testanswers.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO studentdetails(
                        Studentid
                    ) VALUES (?)
                """,(self.answerObject["studentId"],))
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO courseDetails(
                        Studentid,
                        CourseId
                    ) VALUES(?,?)
                """,(self.answerObject["studentId"],self.answerObject["courseId"]))
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO testDetails(
                        CourseId,
                        TestId      
                    ) VALUES(?,?)
                """,(self.answerObject["courseId"], self.answerObject["TestId"]))
                formatedAnswers = ",".join(self.answerObject["answers"])
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO answers(
                        TestId,
                        Answers
                    ) VALUES(?,?)
                """,(self.answerObject["TestId"],formatedAnswers))
                db.commit()
        except sqlite3.Error as error:
            return f"failed to connect to testAnswer db :{error}"
        except Exception as error:
            return f"error on test Answer db: {error}"

# def formateStudentAnswerdata(object):
#     listObj = []
#     for  obj in object:
#             for index ,item in enumerate(obj):
#                 if index == 3:
#                     formateobj = item.split(",")
#                     listObj.append(formateobj)
#     return listObj
def formateCorrectAnswer(answeObject):
    formatedAnswers = []
    testanswers = []
    examanswerList = []
    for obj in answeObject:
        key = list(obj.keys())[0]
        if key == "test":
            details = obj[key]
            for item in details:
                if len(testanswers) == 0:
                    testanswers.append(
                        {
                            "testId":item[0],
                            "answers":[item[2]]
                        }
                    )
                elif len(testanswers) != 0 :
                    for ansobj in testanswers:
                        if ansobj["testId"] == item[0]:
                            ansobj["answers"].append(item[2])
                        else:
                            testanswers.append(
                                {
                                    "testId":item[0],
                                    "answers":[item[2]]
                                }
                            )
        else:
            details = obj[key]
            for item in details:
                if len(examanswerList) == 0:
                    examanswerList.append(
                        {
                            "examId":item[0],
                            "answers":[item[2]]
                        }
                    )
                elif len(examanswerList) != 0 :
                    for ansobj in examanswerList:
                        if ansobj["examId"] == item[0]:
                            ansobj["answers"].append(item[2])
                        else:
                            examanswerList.append(
                                {
                                    "examId":item[0],
                                    "answers":[item[2]]
                                }
                            )
    
    for ans in testanswers:
        formatedAnswers.append(ans)
    else:
        for ans in examanswerList:
            formatedAnswers.append(ans)
    return formatedAnswers


def marks(object1,object2):
    correct_count = sum( 1 for correctAnswer,studentAnswer in  zip(object1,object2) if correctAnswer == studentAnswer)

    return round((correct_count/ len(object1))* 100)
    # for i in range(len(object1)):
    #     if object1[i] == object2[i]:
    #         score += 1
    # return round((score/len(object1))*100)


class AssessmentResults:
    def __init__(self,studentId, courseId):
        self.studentAnswersDetails = []
        self.correctAnswers = []
        self.studentId = studentId
        self.courseId = courseId
        self.studentResults = None
        self.correctResults = None
        # self.examResults = None

    def fetchRightAnswers(self):
        try:
            with sqlite3.connect("testDataBase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    SELECT
                        q.TestId,q.CourseId, a.Answer
                    FROM
                        questionDetails AS q
                    JOIN
                        answer AS a ON a.CourseId == q.CourseId
                    WHERE
                        q.CourseId == ?  
                """,(self.courseId,))
                TestData = cursor.fetchall()
                if TestData:
                    self.correctAnswers.append({"test":TestData})
                else:
                    self.correctAnswers.append({"test":"no test"})
            with sqlite3.connect("examDataBase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    SELECT
                        q.ExamId,q.CourseId,a.Answer
                    FROM
                        questionDetails AS q
                    JOIN
                        answer AS a ON a.CourseId == q.CourseId
                    WHERE
                        q.CourseId == ?           
                """,(self.courseId,))
                Examdata = cursor.fetchall()
                if Examdata:
                    self.correctAnswers.append({"exam":Examdata})
                else:
                    self.correctAnswers.append({"exam":"no answers"})
        except sqlite3.Error as error:
            return f"fetchRightAnswers api failed to connect to  specified database:{error}"
        except Exception as error:
            return f"Error on fetching RightAnswers from the specified database:{error}"
       

    def fetchStudentAnswers(self):

        try:
            with sqlite3.connect("testanswers.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    SELECT
                        s.Studentid,c.CourseId, t.TestId, a.Answers
                    FROM
                        studentdetails as s
                    JOIN
                        courseDetails AS c ON c.Studentid == s.Studentid
                    JOIN
                        testDetails AS t ON t.CourseId == c.CourseId
                    JOIN
                        answers AS a ON a.TestId == t.TestId
                    WHERE
                        s.Studentid == ? AND c.CourseId == ?
                    
                """,(self.studentId, self.courseId))
                TestData = cursor.fetchall()
            if TestData:
                self.studentAnswersDetails.append({"test":TestData})
            else:
                self.studentAnswersDetails.append({"test":"no answers"})

            with sqlite3.connect("studentExamAnswers.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    SELECT
                        s.StudentId,c.courseID,c.ExamId,a.Answers
                    FROM
                        studentDetails AS s
                    JOIN
                        ExamDetails AS c ON c.StudentId == s.StudentId 
                    JOIN
                        Answers  AS a ON a.ExamId == c.ExamId
                    WHERE
                        s.StudentId == ? AND c.courseID == ? 
                """,(self.studentId,self.courseId))
                ExamData = cursor.fetchall()
            if ExamData:
                self.studentAnswersDetails.append({"exam":ExamData})
            else:
                self.studentAnswersDetails.append({"exam":"no results"})

        except sqlite3.Error as error:
            return f" sql Error on fetchRightAnswer api:{error}"
        except Exception as error:
            return f"Error on fetchRightAnswer api:{error}"
    def formateStudentAnswerData(self):
        self.fetchStudentAnswers()
        # print(self.studentAnswersDetails)
        answers = []
        testanswersList = []
        examanswersList = []
        for answerobj in self.studentAnswersDetails:
            key = list(answerobj.keys())[0]
            if key == "test":
                testnaswers = answerobj[key]
                for details in testnaswers:
                    if len(testanswersList) == 0:
                        testanswersList.append({
                        "testId":details[2],
                        "answers":details[3].split(",")
                        
                        })
                    else:
                        
                        for ans in testanswersList:
                            if ans["testId"] == details[2]:
                                continue
                            else:
                                testanswersList.append({
                                    "testId":details[2],
                                    "answers":details[3].split(",")
                                    
                                    })

            else:
                examanswers = answerobj[key]
                for details in examanswers:
                    
                    if len(examanswersList) == 0:
                        examanswersList.append({
                        "examId":details[2],
                        "answers":details[3].split(",")
                        
                        })
                    else:
                        
                        for ans in examanswersList:
                            if ans["examId"] == details[2]:
                                continue
                            else:
                                examanswersList.append({
                                    "examId":details[2],
                                    "answers":details[3].split(",")
                                    
                                    })

        for answ in testanswersList:
            answers.append(answ)
        else:
            for answ in examanswersList:
                answers.append(answ)

        self.studentResults = answers
        
    def formateAnswers(self):
        self.fetchRightAnswers()
        self.formateStudentAnswerData()
        self.correctResults =  formateCorrectAnswer(self.correctAnswers)

    def markResults(self):
        self.formateAnswers()
        
        def makeResultsStructure():
            scores = []
            for object in self.studentResults:
                for key in object:
                    if key == "testId":
                        if len(scores) == 0:
                            scores.append(
                                {
                                    "testId":object[key],
                                    "scores": 0
                                }
                            )
                        else:
                            for obj in scores:
                                for key in obj:
                                    if key == "testId":
                                        if obj[key] == object[key]:
                                            continue
                                        else:
                                            scores.append(
                                                {
                                                    "testId":object[key],
                                                    "scores": 0
                                                }
                                            )
                                    else:
                                        continue
                    elif key == "examId":                      
                        scores.append(
                            {
                                "examId":object[key],
                                "scores": 0
                            }
                        )
                    else:
                        continue
            return scores
        
        

        scoreBody = makeResultsStructure()
        for object in self.studentResults:
            value = list(object.values())
            id = value[0]
            answer = value[1]
            

            for correctObj in self.correctResults:
                correctValues = list(correctObj.values())
                if id in correctValues:
                    correct = correctValues[1]
                    for obj in scoreBody:
                        for key in obj:
                            if obj[key] == id:
                                obj["scores"] = marks(answer,correct)
                else:
                    continue
        return scoreBody
    

class SchoolDatabes:
    def __init__(self,schoolObject):
        self.schoolObjet = schoolObject
    def createTables(self):
        try:

            with sqlite3.connect("schoolsDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS schoolDetails(
                            Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            SchoolId VARCHAR(200) PRIMARY KEY,
                            SchoolName VARCHAR(300)  
                    )
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS SchoolCoordinator(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        SchoolId VARCHAR(200),
                        CoordinatorName VARCHAR(300),
                        FOREIGN KEY(SchoolId) REFERENCES schoolDetails(SchoolId) ON DELETE CASCADE
                        
                    )
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS schoolUrl(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        SchoolId VARCHAR(200),
                        Url TEXT,
                        FOREIGN KEY(SchoolId) REFERENCES schoolDetails(SchoolId) ON DELETE CASCADE
                    )
                """)
                db.commit()
        except sqlite3.Error as error:
            return f"sqlite connection error:{error}"
        except Exception as error:
            return f"schoolDatabase error:{error}"
        else:
            return "succefully created"
            

    def insertIntotables(self):
        try:
            for school in self.schoolObjet:
            
                with sqlite3.connect("schoolsDatabase.db") as db:
                    cursor = db.cursor()
                    cursor.execute("""
                        INSERT INTO schoolDetails(
                            SchoolId,
                            SchoolName         
                        ) VALUES(?,?)
                    """,(school["schoolId"], school["SchoolName"]))
                    cursor.execute("""
                        INSERT INTO SchoolCoordinator(
                            SchoolId,
                            CoordinatorName        
                        ) VALUES(?,?)
                    """,(school["schoolId"], school["SchoolCoordinator"]))
                    cursor.execute("""
                        INSERT INTO schoolUrl(
                            SchoolId,
                            Url
                        )VALUES(?,?)
                    """,(school["schoolId"],school["schoolUrl"]))
                    db.commit()
        except sqlite3.Error as error:
            return f"sqlite error: {error}"
        except Exception as error:
            return f"school databasee error: {error}"
        else:
            return "succefully inserted"
        


def formateSchoolData(object):
    return [{
        "schoolId": object["schID"],
        "SchoolName": object["schName"],
        "SchoolCoordinator":object["schCoordinator"],
        "schoolUrl":object["url"]

    }]



class StudentCourseProject:
    def __init__(self, projectObject,courseId,cohort, projectId) -> None:
        self.projectObject = projectObject
        self.courseId = courseId
        self.cohort = cohort
        self.projectId = projectId
    def createTables(self):
        try:
            with sqlite3.connect("CourseProjectInstructions.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS projectDetails(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        ProjectId VARCHAR(500) PRIMARY KEY,
                        CourseId TEXT,
                        Cohort VARCHAR(500),
                        ProjectTitle TEXT,
                        ProjectDescription TEXT,
                        Deadline VARCHAR(200),
                        StartDate VARCHAR(200)      
                    )
                """)
        except sqlite3.Error as e:
            raise RuntimeError(f"sqlite connection issues:{e}")
        except Exception as error:
            raise RuntimeError(f"faced error while creating student project database:{error}")
    def insertIntoTable(self):
        try:
            with sqlite3.connect("CourseProjectInstructions.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO projectDetails(
                        ProjectId,
                        CourseId,
                        Cohort,
                        ProjectTitle,
                        ProjectDescription,
                        Deadline,
                        StartDate          
                    ) VALUES (?,?,?,?,?,?,?)
                """,(self.projectId,self.courseId,self.cohort, self.projectObject["projectTitle"],self.projectObject["ProjectDescrpition"],self.projectObject["deadLine"],self.projectObject["startDate"]))
                db.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f" connection error while inserting into course project instruction db: {e}")
        except Exception as e:
            raise RuntimeError(f"Error while inserting into  course project instruction db: {e}")
        



class StudentCourseProjectRepoDetails:
    def __init__(self,reponseObject, studentId) -> None:
        self.responseObject = reponseObject
        self.courseId = self.responseObject["courseId"]
        self.projectLink = self.responseObject["projectlink"]
        self.projectId = self.responseObject["projectId"]
        self.cohort = self.responseObject["cohort"]
        self.studentId = studentId
        
    def createTable(self):
        try:
            with sqlite3.connect("StudentCourseProjectDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS StudentProjectResponse(
                            Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            StudentId VARCHAR(300),
                            CourseID TEXT,
                            Cohort VARCHAR(300),
                            ProjectId VARCHAR(500) PRIMARY KEY,
                            GithubProjectRepoLink TEXT
                    )
                """)
        except sqlite3.Error as e:
            raise RuntimeError(f"connection error while creating student course project response db: {e}")
        except Exception as e:
            raise RuntimeError(f"error while creating  student course project response db: {e}")
    def inserIntotable(self):
        try:
            with sqlite3.connect("StudentCourseProjectDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO StudentProjectResponse(
                            StudentId,
                            CourseID,
                            Cohort,
                            ProjectId,
                            GithubProjectRepoLink 
                    ) VALUES (?,?,?,?,?)
                """,(self.studentId,self.courseId,self.cohort,self.projectId,self.projectLink))
        except sqlite3.Error as e:
            raise RuntimeError(f"connection error while inserting into student course project response db: {e}")
        except Exception as e:
            raise RuntimeError(f"error while inserting into student course project response db: {e}")
        


class PartnershipDatabase:
    def __init__(self, dataObject) -> None:
        self.dataObject = dataObject
        self.firstName = self.dataObject["firstName"]
        self.sirName = self.dataObject["sirName"]
        self.phoneNumber = self.dataObject["phoneNumber"]
        self.email = self.dataObject["email"]
        self.country = self.dataObject["country"]
        self.typeOfPartnership = self.dataObject["typeOfPartnership"]
    def CreateTables(self):
        try:
            with sqlite3.connect("partnersDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS partnerDetails(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        ResponseId INTEGER PRIMARY KEY AUTOINCREMENT,
                        FirstName VARCHAR(200),
                        LastName VARCHAR(200)         
                    )
                """)

                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS partnersContacts(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        ResponseId INTEGER PRIMARY KEY AUTOINCREMENT,
                        PhoneNumber VARCHAR(200),
                        Email VARCHAR(500),
                        CountryLocation VARCHAR(500)
                    )
                """)

                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS morePartnershipDetails(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        ResponseId INTEGER PRIMARY KEY AUTOINCREMENT,
                        TypeOfPartnership VARCHAR(200)          
                    )
                """)

        except sqlite3.Error as error:
            raise RuntimeError(f"Connection error while connecting to partnership db: {error}")
        except Exception as error:
            raise RuntimeError(f"Faced error while creating partnership details db: {error}")
    def insertIntoTable(self):
        try:
            with sqlite3.connect("partnersDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO partnerDetails(
                        FirstName,
                        LastName 
                    ) VALUES (?,?)
                """,(self.firstName, self.sirName))
                cursor.execute("""
                    INSERT INTO partnersContacts(
                        PhoneNumber,
                        Email,
                        CountryLocation          
                    ) VALUES(?,?,?)
                """,(self.phoneNumber,self.email,self.country))
                cursor.execute("""
                    INSERT INTO morePartnershipDetails(
                        TypeOfPartnership          
                    ) VALUES(?)
                """,(self.typeOfPartnership,))
        except sqlite3.Error as error:
            raise RuntimeError(f"connection error while inserting into partnership db: {error}")
        except Exception as error:
            raise RuntimeError(f"error while inserting into partnership db:{error}")



            







            
            

        

      

    
        
        





           
           
           

