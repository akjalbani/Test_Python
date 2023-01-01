'''
This script will create an email message with the specified subject and body, 
and it will use the smtplib library to connect to the email server and send the message. 
You will need to modify the script to use the correct email address and password for your account, 
as well as the correct SMTP server and port for your email provider.

To send a text message alert, you can use a library or service that provides access to the SMS gateway of a mobile carrier.
For example, you could use the twilio library to send text messages using the Twilio API. 
You will need to sign up for a Twilio account and purchase a phone number in order to use this service.

'''

import smtplib

# Set the email address and password for the account you want to use to send the email
from_email = "you@example.com"
password = "your-email-password"

# Set the recipient's email address and the subject and body of the message
to_email = "alerts@example.com"
subject = "Suspicious Activity Alert"
body = "There has been suspicious activity detected on the server. Please investigate immediately."

# Create the message using the email library's Message class
message = email.message.Message()
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subject
message.set_payload(body)

# Connect to the email server and send the message
smtp_server = smtplib.SMTP("smtp.example.com")
smtp_server.login(from_email, password)
smtp_server.sendmail(from_email, to_email, message.as_bytes())
smtp_server.quit()
