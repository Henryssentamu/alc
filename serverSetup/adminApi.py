import sqlite3


class AdminCredientalApi:
    {'employeeId': 'qwerty', 'admincode': 'q21332e3', 'password': 'weeeeww'}
    def __init__(self,adminObject) -> None:
        self.adminObject = adminObject
        self.employeeId = self.adminObject["employeeId"]
    def fetchCredientals(self):
        try:
            with sqlite3.connect("adminlogincrediential.bd") as db:
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
                        e.EmployeeId == ?       
                """,(self.employeeId,))
                data = cursor.fetchall()
        except sqlite3.Error as error:
            raise RuntimeError(f"sql connection error on admin crediental api:{error}")