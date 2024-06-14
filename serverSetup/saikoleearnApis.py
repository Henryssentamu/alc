import sqlite3
class CourseDetailsApi:
    def __init__(self) -> None:
        self.schoolId = None

    def convertCourseToInt(self,value):
        """
            this function tries to convert return course price to int or float otherwise it keep it a string
            if price = free
            arg = price value retrived from database 
        """
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value
    def fetchAvaibleCourses(self, schoolId):
        """ 
            this function returns availabe courses give a school id
            And on calling you provida school id which is a str
        """
        self.schoolId = schoolId
        try:
            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    select
                        C.courseId,
                        C.schoolId,
                        C.courseName,
                        C.courseDuration,
                        C.routFunction,
                        P.coursePrice,
                        P.coursePriceIds,
                        I.courseImageLink,
                        D.courseDiscription
                               
                               
                    FROM
                        courseDetails AS C
                    JOIN
                        coursePriceIdDetails AS P ON P.courseId == C.courseId
                    JOIN
                        courseImageLinks AS I ON I.courseId == C.courseId
                    JOIN
                        courseDiscription AS D ON D.courseId == C.courseId
                    WHERE
                        C.schoolId == ?   
                """,(self.schoolId,))
                data = cursor.fetchall()
                return data
        except sqlite3.Error as error:
            raise RuntimeError(f"sql connection error while retriving available courses:{error}")
        except Exception as error:
            raise RuntimeError(f"un an excepted error while connecting to course database:{error}")
    def courseTuitionDetails(self,courseId):
        """
            arg: course id, str
            return: a dictionary of priceId and price 
        """
        self.courseId = courseId
        try:
            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                        SELECT
                            coursePriceIds,coursePrice
                        FROM
                            coursePriceIdDetails
                        WHERE
                            courseId == ?
                """,(self.courseId,))
                data = cursor.fetchone()
                price = self.convertCourseToInt(data[1])
                details = {"priceId":data[0],"price":price}
                
                return details
        except sqlite3.Error as e:
            raise RuntimeError(f"connection error while retriving course price detials:{e}")
        except Exception as error:
            raise RuntimeError(f"error while retriving course price details: {error}")
    def numberOfAvailableCourses(self):
        try:
            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    SELECT
                        count(*)
                    FROM
                        courseDetails  
                """)
                Data = cursor.fetchone()
                if Data:
                    return {"numberOfAvailableCourses":Data}
        except sqlite3.Error as error:
            raise RuntimeError(f"sql error while fetching numberOfAvailableCourses: {error}")
        except Exception as error:
            raise RuntimeError(f"an Unexcepted error while fetching numberOfAvailableCourses: {error}")
        


class StudentApi:
    def __init__(self) -> None:
        pass
        
    def numberOfStudents(self):
        try:
            with sqlite3.connect("StudentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    SELECT
                        count(*)
                    FROM
                        studentDetails
                """)
                data = cursor.fetchone()
                if data:
                    return {"numberOfStudents":data}
        except sqlite3.Error as error:
            raise RuntimeError(f"sql connection error while connecting to StudentDetails.db to fetch number of student:{error}")
        except Exception as error:
            raise RuntimeError(f"error while fetching number of students on StudentDetails.db:{error}")
        

class AdminCredientalApi:
    {'employeeId': 'qwerty', 'admincode': 'q21332e3', 'password': 'weeeeww'}
    def __init__(self,adminObject) -> None:
        self.adminObject = adminObject
        self.employeeId = self.adminObject["employeeId"]
        self.adminCode = self.adminObject["admincode"]
        self.password = self.adminObject["password"]
        self.fetchedDetails = None
    def fetchCredientals(self):
        try:
            with sqlite3.connect("admincredentials.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    SELECT
                        e.EmployeeId,a.AdminCode, p.Password
                    FROM
                        admin AS e
                    JOIN
                        admincodeInfo AS a ON a.EmployeeId == e.EmployeeId
                    JOIN
                        passwords AS p ON p.EmployeeId == e.EmployeeId
                    WHERE
                        e.EmployeeId == ? AND a.AdminCode ==? AND p.Password ==?       
                """,(self.employeeId, self.adminCode, self.password))
                data = cursor.fetchone()
                if data:
                    self.fetchedDetails = data
        except sqlite3.Error as error:
            raise RuntimeError(f"sql connection error on admin crediental api:{error}")
        except Exception as error:
            raise RuntimeError(f"un an Expected error while fetching admin credientals: {error}")
        
    def is_admin(self):
        # triger data fetch
        try:
            self.fetchCredientals()
            if self.fetchedDetails:
                return True
            else:
                return False 
        except Exception as error:
            raise RuntimeError(f"un an expected error while comparing admin credientals:{error}")
        

class SchoolApi:
    def __init__(self) -> None:
        
        pass
    def numberOfSchools(self):
        try:
            with sqlite3.connect("schoolsDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    SELECT
                        count(*)
                    FROM
                        schoolDetails   
                """)
                data = cursor.fetchone()
                if data:
                    return {"numberOfSchools":data}
        except sqlite3.Error as error:
            raise RuntimeError(f"sql error while connecting to school database in school api:{error}")
        except Exception as error:
            raise RuntimeError(f"error while getting number of schools in school api: {error}")



