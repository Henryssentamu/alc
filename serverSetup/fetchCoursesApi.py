import sqlite3

from flask import jsonify


class FetchAvaibleCourses:
    """ this class returns availabe course give a school id
        And on calling you provid an object containing school id with a key 'schoolId'
    """

    def __init__(self,object) -> None:

        self.object = object
        self.schoolId = object["schoolId"]
    def availabCourses(self):
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
        

class CheckPaidCourse:
    """this class returns price details of acourse give price id"""
    def __init__(self, pricId) -> None:
        self.priceId = pricId
    def retivePriceDetails(self):
        try:
            with sqlite3.connect("courseDatabase.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                        SELECT
                            coursePrice
                        FROM
                            coursePriceIdDetails
                        WHERE
                            coursePriceIds == ?
                """(self.priceId))
                data = cursor.fetchone()
                return data
        except sqlite3.Error as e:
            raise RuntimeError(f"connection error while retriving course price detials:{e}")
        except Exception as error:
            raise RuntimeError(f"error while retriving course price details: {error}")
        

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

