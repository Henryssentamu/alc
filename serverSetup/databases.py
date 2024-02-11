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