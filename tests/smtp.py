#! /usr/local/bin/python
import os
import mimetypes
from email.message import EmailMessage
import dotenv

dotenv.load_dotenv("../local.env")
SMTPserver =os.getenv("SMTPserver")
sender =   os.getenv("sender")
destination = ['exu51@stuy.edu']
USERNAME =os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'


# Function to attach a file
def attach_file(msg, filepath):
    filename = os.path.basename(filepath)
    mimetype, _ = mimetypes.guess_type(filepath)
    if mimetype is None:
        mimetype = 'application/octet-stream'
    maintype, subtype = mimetype.split('/', 1)

    with open(filepath, 'rb') as fp:
        msg.add_attachment(fp.read(),
                           maintype=maintype,
                           subtype=subtype,
                           filename=filename)

content="""
<!DOCTYPE html>
<html>
<head>
    <meta name="color-scheme" content="light only">
    <meta name="supported-color-schemes" content="light only">
</head>
<body
    style="text-align: center; font-family: 'Helvetica Neue', sans-serif; font-size: 12; color: #0629B0 !important; margin: 0; padding: 0; background-color: #FFFEF9 !important;">
    <div style="max-width: 500px; margin: 0 auto; padding: 50px;">
        <div style="margin-bottom: 50px;">
            <img src="https://github.com/Junior-Caucus-SU/TicketCatcher/blob/main/stuy_logo.png?raw=true"
                alt="School Logo" style="max-width: 100px;">
        </div>
        <div style="font-size: larger;">
            <p style="padding-bottom: 10px;">Hi NAME!</p>
            <p style="padding-bottom: 10px;">We're excited to confirm your registration for Stuyvesant Junior Prom 2024, and we're looking forward to welcoming you to an unforgettable evening of fun. Below is your private barcode for entry to the event. Please ensure you save this email as this barcode will be scanned for your admission.</p>
            <p style="padding-bottom: 10px;">A follow-up email will be sent to you soon containing detailed information regarding the event. Until then!</p>
            <p>Cheers,<br>Elias, Will, and the Junior Caucus</p>
        </div>
    </div>
</body>
</html>"""

subject="Sent from Python"

import sys
import re

from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

# old version
# from email.MIMEText import MIMEText
from email.mime.text import MIMEText
from email.utils import formatdate


try:
    msg = EmailMessage()
    msg['Subject']= subject
    msg['From']   = sender # some SMTP servers will do this automatically, not all
    msg['Date'] = formatdate(localtime=True)  # Add the date header
    msg['To'] = destination[0]  # Add the sendee header
    msg['List-Unsubscribe'] = "<mailto:no-reply@junior.stuysu.org?subject=unsubscribe>"  # Add the unsubscribe header
    
    
    msg.set_content(content, subtype="html")
    
    attach_file(msg, "image.png")

    
    conn = SMTP(SMTPserver)
    conn.set_debuglevel(False)
    conn.login(USERNAME, PASSWORD)
    print("sucess")
    try:
        conn.sendmail(sender, destination, msg.as_string())
        print("sucess")
    finally:
        conn.quit()


except Exception as e:
    print("Mail failed:", str(e))
    sys.exit("Mail failed; %s" % str(e))
    
    