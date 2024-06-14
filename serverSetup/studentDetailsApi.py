import sqlite3


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