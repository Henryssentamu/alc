
import smtplib
from email.message import EmailMessage



def sendEmail(Email,sPassword,studentRigNo):
    # studentEmail ="henryphillip61@gmail.com"
    # studentPassword = "weeeee"
    # studentRigNo="/1234"
    sender = "ssentamuhenry00@gmail.com"
    password = "wohg wzqz zmte pyqp"
    msg = EmailMessage()
    msg.set_content(f"Your saikolearn login details\n\n Your RegNo:{studentRigNo}\n password:{sPassword}")
    msg["Subject"] ="Student Credentials"
    msg["From"] = sender
    msg["To"] = Email

    try:

        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=sender,password=password)
            connection.send_message(msg=msg)
            # print("sent")
    except Exception as error:
        print(f"failed to send student credentials:{str(error)}")

class SendPartnershipEmails:
    def __init__(self,partnersDetails) -> None:
        self.sender = "ssentamuhenry00@gmail.com"
        self.password = "wohg wzqz zmte pyqp"
        self.partnerEmail = partnersDetails["email"]
        self.partnerFirstName = partnersDetails["firstName"]
        self.partnerSirName = partnersDetails["sirName"]
        self.partnerPhoneNumber = partnersDetails["phoneNumber"]
        self.partnerCountry = partnersDetails["country"]
        self.typeOfPartnership = partnersDetails["typeOfPartnership"]
        self.moreInfor = partnersDetails["moreInfo"]
        self.expectation = partnersDetails["expectionFromPartnership"]
        self.affriation = partnersDetails["affriation"]
        self.position = partnersDetails["position"]
        self.funding = partnersDetails["funding"]
        self.purposeOfpartnership = partnersDetails["purposeOfpartnership"]
        
    def sendPartnersDetailsTo_saikolearn_account(self):
        
        msgObject = EmailMessage()
        msgObject.set_content(f"NEW PARTNER \n\n Name: { self.partnerFirstName}, {self.partnerSirName} \n\n CONTACTS DETAILS:\n\n PhoneNumber: {self.partnerPhoneNumber}\n\n Email: {self.partnerEmail}\n\n Country Of origin: {self.partnerCountry} \n\n Type of partnership: {self.typeOfPartnership} \n\n Purpose of the partnership: {self.purposeOfpartnership}\n\n Expectation from the partnership: {self.expectation}\n\n PARTNER' CURRENT OCCUPTION DETAILS \n\n Occuption: {self.affriation},\n\n Position: {self.position}.\n\n MORE INFO ABOUT THE PARTNERSHIP:\n\n More Info: {self.moreInfor}")
        msgObject["Subject"] = "PARTNER'S DETAILS"
        msgObject["From"] = self.sender
        msgObject["To"] = "ssentamuhenry61@gmail.com"

        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as smsConnect:
                smsConnect.starttls()
                smsConnect.login(user=self.sender,password= self.password)
                smsConnect.send_message(msg= msgObject)
        except Exception as error:
            raise RuntimeError(f"failed to send partner's details to saikolearn email:{error}")
    def sendMessageReceivedResponseToPartner(self):
        msg = EmailMessage()
        msg.set_content(f"Dear: {self.partnerSirName} \n\n Thank you immensely for offering to support ALICIA LEARNING CENTER's (saikolearn) program. Your interest in providing scholarships to our \n\n students is deeply appreciated. We're eager to discuss collaboration and will be reaching out shortly to \n\n coordinate. Your generosity will undoubtedly transform lives.\n\n Warm regards \n\n saikolearn")
        msg["Subject"] = "Heartfelt Thanks for Your Support Offer To saikolearn"
        msg["From"] = self.sender
        msg["To"] = self.partnerEmail
        try:
            with smtplib.SMTP("smtp.gmail.com",port= 587) as smsconnection:
                smsconnection.starttls()
                smsconnection.login(user=self.sender,password=self.password)
                smsconnection.send_message(msg=msg)
        except Exception as error:
            raise RuntimeError(f"failed to send thanks message to partner:{error}")


class SendInqurry:
    def __init__(self, inqurryDetails) -> None:
        self.Name = inqurryDetails["Name"]
        self.Email = inqurryDetails["Email"]
        self.phoneNumber = inqurryDetails["PhoneNumber"]
        self.message = inqurryDetails["Message"]
        self.sender = "ssentamuhenry00@gmail.com"
        self.password = "wohg wzqz zmte pyqp"
    def sendInquery(self):
        InqueryMessage = EmailMessage()
        InqueryMessage.set_content(f"A person with the following details sent this message.\n\n Name: {self.Name},\n\n Message:{self.message}\n\n CONTACT DETAILS \n\n PhoneNumber: {self.phoneNumber}\n\n Email:{self.Email}\n\n ")
        InqueryMessage["Subject"] = "Message From Contact Us Page"
        InqueryMessage["From"] = self.sender
        InqueryMessage["To"] = self.Email
        try:
            with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
                connection.starttls()
                connection.login(user= self.sender,password=self.password)
                connection.send_message(msg=InqueryMessage)
        except Exception as error:
            raise RuntimeError(f"failed to send message/ inquirry to saikolearn webmail:{error}")
        
        

