import smtplib, ssl, os, email
from app.config import SSL_PORT,SMTP_SERVER,SENDER_EMAIL,RECEIVER_EMAIL,SENDER_EMAIL_PSW
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





#Test funct
def setMessage(sender, subject, message):
    
    msg = MIMEMultipart()
    msg["Subject"] = """[WS] {0}""".format(subject) #Add limit to the size.
    msg["From"] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    ## HTML 
    html = """\
    <html>
    <body>
        <h2>New Message!</h2>
        <div>
            <h4>Subject: {1}</h4>
            <hr>
            
            <p>
                <b>Messagge: </b>
                <br>
                {0}
            </p>
        </div>
    </body>
    </html>
    """.format(message , subject)

    body_html = MIMEText(html, 'html')
    msg.attach(body_html)  # attaching to msg
    
    return msg

def sendEmail(message):
    status = -1  #We're pessimistic
    context = ssl.create_default_context()
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SSL_PORT)
        server.ehlo()  # check connection
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # check connection
        server.login(SENDER_EMAIL, SENDER_EMAIL_PSW)

        # Send email here
        ret = server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
        status = -1 if len(ret) > 0 else 0 #-1 mail sent with errors 0 otherwhise
        
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
        return status

