import datetime, random



class GenerateCoursePaymentRefrenceNumber:
    def __init__(self,studentId) -> None:
        self.studentId = studentId
        self.refrenceGeneratedDateDetails = datetime.datetime.now()
    # def conver_str_to_unicode(self):
    #     unicode = ""
    #     for char in self.studentId:
    #         unicode + str(ord(char))
    #     return unicode
        
    def sortStudentId(self):
        modifiedId = ""
        removedChar = self.studentId.split("/")
        for string in removedChar:
            modifiedId += string
        return modifiedId
        
    def makeRefrence(self):
        try:
            modifiedStudentId = self.sortStudentId()
        except ValueError as error:
            print(f" there is a possibility that the sortStudentId function did not return anything: investigate the error:{error}")
        except Exception as error:
            print(f"investiaget this error from the sortStudentId function:{error}")
        try:
            year = self.refrenceGeneratedDateDetails.year
            month = self.refrenceGeneratedDateDetails.month
            day = self.refrenceGeneratedDateDetails.day
            hour = self.refrenceGeneratedDateDetails.hour
            minutes = self.refrenceGeneratedDateDetails.minute
            seconds = self.refrenceGeneratedDateDetails.second

            number = modifiedStudentId + str(year) + str(month) +str(day) +str(hour) + str(minutes) +str(seconds)

            reshuffle = list(number)
            random.shuffle(reshuffle)
            
            refrenceNumber = "".join(reshuffle)
            return refrenceNumber
        except Exception as error:
            print(f" it is possible that datetime module or shuffle() of random module did not work as expected. investigate the error: {error}")
    