import os
import dotenv
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

with open("Content.html", "r") as file:
    data = file.read()

dotenv.load_dotenv("../local.env")

message = Mail(
    from_email=os.getenv("SEND_EMAIL"),
    to_emails=os.getenv("SEND_EMAIL"),
    subject='JProm Test 1',
    html_content=f"{data}")

try:
    sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
