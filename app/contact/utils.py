import smtplib, ssl, os
from app.config import SSL_PORT,SMTP_SERVER,SENDER_EMAIL,RECEIVER_EMAIL,SENDER_EMAIL_PSW


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
    #TODO add better error handling
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, SSL_PORT, context=context) as server:
        server.login(SENDER_EMAIL, SENDER_EMAIL_PSW)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)




