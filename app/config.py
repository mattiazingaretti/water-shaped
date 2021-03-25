import os


#CONSTANTS
SSL_PORT = os.environ["SSL_PORT"]
SMTP_SERVER = os.environ["SMTP_SERVER"] 
SENDER_EMAIL = os.environ["MAIL_SENDER_ADD"] 
RECEIVER_EMAIL = os.environ["MAIL_RECEIVER_ADD"] 
SENDER_EMAIL_PSW = os.environ["MAIL_SENDER_PSW"] 


#APP
SECRETE_KEY = os.environ["FLASK_SK"]

