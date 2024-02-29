import smtplib
from email.message import EmailMessage

import email_inputs


#  username, password

email_adress = email_inputs.email_adress
password = email_inputs.password

def send_email(email_adress):
    with open('textfile.txt') as fp:
        msg = EmailMessage()
        msg.set_content(fp.read())
    
    msg['Subject'] = 'Test'
    msg['From'] = email_adress
    msg['To'] = email_adress

    
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit
    
send_email(email_adress)