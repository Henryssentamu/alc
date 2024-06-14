
import sqlite3
class GetStudent:
    def __init__(self, studentId,password) :
        self.studentId = studentId
        self.password = password
    def is_authenticated(self):
        try:
            with sqlite3.connect("StudentDetails.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                    SELECT
                        s.studentId,
                        p.password
                    FROM
                        studentDetails as s
                    JOIN
                        studentPasswords as p ON s.studentId == p.studentId
                    WHERE
                        s.studentId == ? AND p.password == ? 
                """,(self.studentId, self.password))
                student = cursor.fetchone()
                student = student[0]
                # print(student)
                if student:
                    return True
                return None
        except sqlite3.Error as error:
            print(f"there is a possibility that the app failed to connect to Student details database:{error}")
        except Exception as error:
            print(f"investiage this error related to student datails database:{error}")


# user = GetStudent("/87","123")
# a = user.is_authenticated()
# print(a)
        
