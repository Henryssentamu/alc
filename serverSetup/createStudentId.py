import datetime
import random

class CreateStudentId:
    numberOfStudent = 0
    def __init__(self) -> None:
        self.date_time = datetime.datetime.now()
        self.year = self.date_time.year
        CreateStudentId.numberOfStudent += 1
        self.studentNumber = str(CreateStudentId.numberOfStudent).zfill(4)
    def makeStudentId(self):
        regno = str(self.year)[2:] + "/" + "A"+ "/" + self.studentNumber + "/" +"ps"

        return regno
    
