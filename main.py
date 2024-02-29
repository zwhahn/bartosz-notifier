import smtplib, ssl
import email_inputs

HOST = 'smtp-mail.outlook.com'  # SMTP server domain of outlook
PORT = 587

FROM_EMAIL = email_inputs.email_adress
TO_EMAIL = email_inputs.email_adress
PASSWORD = email_inputs.password

MESSAGE = """Subject: Python script email
Hello World"""

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()  # ping server and check if it's running
print(f"Echoing the server: {status_code}, {response}")

status_code, response = smtp.starttls()  # Establish connection
print(f"Starting TLS connection: {status_code}, {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)  # Sign into email
print(f"Logging in: {status_code}, {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit()

