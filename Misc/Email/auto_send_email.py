# how to send an email using python script
# This will run on IDLE or pycharm, it will not run on REPL.IT
# you have install packages
# Do not send too many emails- email client may block your address
# the code is written for only learning purpose,Do not use code for any malcious activity
# you need smtp address of the email client to send an email- if you want to send email from gmail account you need to change setting to low security
# version 1.0
# @A.A.Jalbani

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr='please add senders email address'
to_addr= ['receiver1@emailaddress.com','receiver2@emailaddress.com']  # you can add receiver addresses here

msg=MIMEMultipart()
msg['From']=from_addr
msg['To']=" ,".join(to_addr)
msg['subject']='Hello programmer'

body='Dear Friend, This is a Test message from XYZ using python!!!!'

msg.attach(MIMEText(body,'plain'))

email='sender email address / user id'   # for example abc@outlook.com
password='sender password'  # password of your email address

mail=smtplib.SMTP('smtp address of your email client',587)  # for example for outlook: smtp.office365.com
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=msg.as_string()
mail.sendmail(from_addr,to_addr,text)
mail.quit()

#####################################

