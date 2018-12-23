import smtplib
import random

email_sender = 'your_email_address'
email_passwd = 'your_email_password'


def send_validation_code(email):
    #validation_code = random.randint(10000, 99999)
    validation_code = 11111
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(email_sender, email_passwd)
        server.sendmail(email_sender, email, "Your validation code is: "+str(validation_code))
    except:
        pass
    return validation_code
