import sqlite3


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

