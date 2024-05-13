import datetime
import random
import sqlite3

class CreateStudentId:
    
    def __init__(self) -> None:
        self.date_time = datetime.datetime.now()
        self.year = self.date_time.year
        self.currentNumber = self.getCurrentNumberOFRegisteredStudents()
        self.number = self.currentNumber + 1
        self.studentNumber = str(self.number).zfill(4)
        print(self.studentNumber)

    def getCurrentNumberOFRegisteredStudents(self):
        try:
            with sqlite3.connect("StudentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    SELECT
                        COUNT(*)
                    FROM
                        studentDetails
                """)
                number = cursor.fetchone()[0]
        except sqlite3.Error as e:
            raise RuntimeError(f"connection error whietting number of registered students: {e}")
        except Exception as error:
            raise RuntimeError(f"error while getting number of registered students: {error}")
        return number
    def makeStudentId(self):
        regno = str(self.year)[2:] + "/" + "A"+ "/" + self.studentNumber + "/" +"ps"

        return regno
    

class CreatePaperIds:
    def __init__(self, courseId, cohort) -> None:
        self.courseId = courseId
        self.cohort = cohort
        self.currentTime = datetime.datetime.now()
        self.year  = str(self.currentTime.year)
    def testId(self):
        testId = "test" + self.year + self.courseId[5: ] + self.cohort
        return testId
    def examId(self):
        exam = "exam" + self.year + self.courseId[5: ] + self.cohort
        return exam
    
class GenerateProjectId(CreatePaperIds):
    def __init__(self, courseId, cohort) -> None:
        super().__init__(courseId, cohort)

    def projectid(self):
        id = self.year + "proj"+self.courseId[8: ] + self.cohort[3:]
        return id