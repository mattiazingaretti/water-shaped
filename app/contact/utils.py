import smtplib, ssl, os
from app.config import SSL_PORT,SMTP_SERVER,SENDER_EMAIL,RECEIVER_EMAIL,SENDER_EMAIL_PSW

#THis is a test comment
def setMessage(sender, subject, message):
    message ="""Subject: [WS] Someone wants to talk to you.
    Who ? : {0} \n  What he\she wants ? : {1} \n
    \n
    \n
    {2}
    \n
    """.format(sender, subject, message)
    return message

def sendEmail(message):
    with smtplib.SMTP(SMTP_SERVER) as server:
        server.login(SENDER_EMAIL, SENDER_EMAIL_PSW)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
    



