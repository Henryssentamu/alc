
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
    def __init__(self, courseId,courseName,coursePrice,coursePriceId, courseImageLink,courseDiscription) -> None:
        self.courseId = courseId
        self.courseName = courseName
        self.coursePrice = coursePrice
        self.coursePriceId = coursePriceId
        self.courseImageLink = courseImageLink
        self.courseDiscription = courseDiscription
    def createTables(self):
        try:

            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS courseDetails(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        courseId TEXT PRIMARY KEY,
                        courseName VARCHAR(200)
                    )
                """)
            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS coursePriceIdDetails(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        coursePriceIds TEXT PRIMARY KEY,
                        courseId TEXT,
                        coursePrice INTERGER,
                        FOREIGN KEY (courseId) REFERENCES courseDetails(courseId)   
                    )
                """)

            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS courseImageLinks(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        courseImageLink TEXT,
                        courseId TEXT,
                        FOREIGN KEY(courseId) REFERENCES courseDetails(courseId)
                    )
                """)
            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS courseDiscription(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        courseId TEXT,
                        courseDiscription TEXT,
                        FOREIGN KEY(courseId) REFERENCES courseDetails(courseId)
                    )
                """)
        except Exception as error:
            print(f"somthing happened in creating course detail database: {error}")
    def insertIntoTables(self):
        try:
            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO courseDetails(
                        courseID,
                        courseName
                    ) VALUES(?,?)
                """,(self.courseId,self.courseName))
                db.commit()
            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO coursePriceIdDetails(
                        coursePriceIds,
                        courseId,
                        coursePrice  
                    )  VALUES(?,?,?)
                """,(self.coursePriceId,self.courseId,self.coursePrice))
                db.commit()
            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO courseImageLinks(
                        courseImageLink,
                        courseId 
                    ) VALUES(?,?)
                """,(self.courseImageLink, self.courseId))
                db.commit()
            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO courseDiscription(
                        courseId,
                        courseDiscription
                    ) VALUES(?,?)
                """,(self.courseId,self.courseDiscription))
                db.commit()
        except Exception as error:
            print(f"faced chalenge in inserting data into course details. {error}")

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
                        Topic
                        
                             
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
                        CourseId
                    )
                """)
        except sqlite3.Error as error:
            print(f"connection error:{error}")
        except Exception as error:
            print(f"error occured in creating liveseesion database:{error}")
    def insertIntoliveSessionsTable(self,Date,SessionTime,CourseID,link, InstructorName,Topic):
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
                        Topic
                    ) VALUES (?,?,?,?,?,?)
                """,(Date,SessionTime,CourseID,link, InstructorName,Topic))
                db.commit()
        except sqlite3.Error as error:
            print(f"faced error while creating recorded link table:{error}")
        except Exception as error:
            print(f"error occured while insertint into liveSessions table :{error}")


    def insertIntorecordedLinksTable(self,link,DateOfRecording,SessionTitle,TopicCovered, CourseId):
        try:
            with sqlite3.connect("liveSessionLinks.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    INSERT INTO recordedLinks(
                        DateOfRecording,
                        Link,
                        SessionTitle,
                        TopicCovered,
                        CourseId
                    ) VALUES (?,?,?,?,?)
                """,(DateOfRecording,link,SessionTitle,TopicCovered,CourseId))
                db.commit()
        except sqlite3.Error as error:
            print(f"faced error while inserting into recorded link table:{error}")
        except Exception as error:
            print(f"error occured while inserting into liveSessions table :{error}")



class Exams:
    def __init__(self, questionObject,courseId) -> None:
        self.questionObject = questionObject
        self.courseId = courseId
    def createTables(self):
        try:
            with sqlite3.connect("examDataBase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS questionDetails(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        QuestionId INTEGER PRIMARY KEY AUTOINCREMENT,
                        CourseId TEXT,
                        Question TEXT       
                    )
                        
                """)

            with sqlite3.connect("examDataBase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS options(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        OptionId INTEGER PRIMARY KEY AUTOINCREMENT,
                        CourseId TEXT,
                        Options TEXT,
                        FOREIGN KEY(CourseId) REFERENCES questionDetails(CourseId)   
                    )
                        
                """)

            with sqlite3.connect("examDataBase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS answer(
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        AnswerId INTEGER PRIMARY KEY AUTOINCREMENT,
                        CourseId TEXT,
                        Answer TEXT,
                        FOREIGN KEY(CourseId) REFERENCES questionDetails(CourseId)   
                    )
                        
                """)
        except sqlite3.Error as error:
            print(f"failed to connect to exam database:{error}")
        except Exception as error:
            print(f"exam data base error:{error}")
    
    def insertIntoTable(self):
        for object in self.questionObject:
            self.question = object["question"]
            self.options = object["options"]
            self.answer = object["correct_answer"]
            StringOptions = ",".join(self.options)
            try:
                with sqlite3.connect("examDataBase.db") as db:
                    cursor = db.cursor()
                    cursor.executemany("""
                        INSERT INTO  questionDetails(
                            CourseId,
                            Question         
                        ) VALUES (?,?)
                            
                    """,(self.courseId, self.question))
                    db.commit()

                with sqlite3.connect("examDataBase.db") as db:
                    cursor = db.cursor()
                    cursor.executemany("""
                        INSERT INTO  options(
                            CourseId,
                            Options,         
                        ) VALUES (?,?)
                            
                    """,(self.courseId, StringOptions))
                    db.commit()
                with sqlite3.connect("examDataBase.db") as db:
                    cursor = db.cursor()
                    cursor.executemany("""
                        INSERT INTO  answer(
                            CourseId,
                            Answer,         
                        ) VALUES (?,?)
                            
                    """,(self.courseId, self.answer))
                    db.commit()

                
            except sqlite3.Error as error:
                print(f"Error On inserting into Exam databese :{error}")
                return f"Error On inserting into Exam databese :{error}"
            except Exception as error:
                print(f"Error On inserting into Exam databese :{error}")
                return f"Error On inserting into Exam databese :{error}"
