import random

class CreateStudentId:
    def __init__(self, sirName) -> None:
        self.sirName = sirName
    def generateRandomNumber(self):
        return random.randint(1,100)
    def makeStudentId(self):
        number = self.generateRandomNumber()
        # if self.generateRandomNumber() == number:
        #     number = self.generateRandomNumber()
        # numberToUse = number
        return f"{self.sirName[:4]}/{number}"