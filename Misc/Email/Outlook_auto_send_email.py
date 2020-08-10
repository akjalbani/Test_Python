# Check before running
# This script will send email from your outlook email client, make sure that outlook is already installed and configured with your email
# if you outlook contains many email profile, it will send email with default outlook profile.
# outlook client should be running on you host os
# you may need to install pywin32 python module using pip command
# go to windows command line and write pip install pywin32
# Checked on python IDEL, it should also run on pycharm
# dont use repl.it for this

# pip install pywin32

import win32com.client as client

outlook = client.Dispatch('Outlook.Application')
message = outlook.CreateItem(0)
message.To = 'Reciever email'
message.CC = 'cc to another email address'
#message.BCC = 'bcc to another email'

message.Subject = 'Type Subject of email here'

html_body = """
    <div>
        <h1 style="font-family: 'Lucida Handwriting'; font-size: 56; font-weight: bold; color: #9eac9c;">
            Hello Friend!
        </h1>
        <h2 style="font-family: 'Lucida Handwriting'; font-size: 56; font-weight: bold; color: #9eac9c;">
         Write you message herer</h2>
        <span style="font-family: 'Lucida Sans'; font-size: 20; color: #8d395c;">
           You can you different html formatting in your message body. 
            
        </span>
    </div><br>
    <div>
        <img src="https://files.realpython.com/media/Newbie_Watermarked.a9319218252a.jpg" width=70%>
    </div>
    """
message.HTMLBody = html_body
message.Send()
