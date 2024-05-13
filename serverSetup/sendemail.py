
import smtplib
from email.message import EmailMessage



def sendEmail(Email,sPassword,studentRigNo):
    # studentEmail ="henryphillip61@gmail.com"
    # studentPassword = "weeeee"
    # studentRigNo="/1234"
    sender = "ssentamuhenry00@gmail.com"
    password = "wohg wzqz zmte pyqp"
    msg = EmailMessage()
    msg.set_content(f"Your alc login details\n\n Your RegNo:{studentRigNo}\n password:{sPassword}")
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

class sendPartnershipEmails:
    def __init__(self) -> None:
        pass

        

