
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
import dotenv
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

dotenv.load_dotenv("../local.env")

message = Mail(
    from_email=os.getenv("SEND_EMAIL"),
    to_emails=os.getenv("SEND_EMAIL"),
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')

with open("image.png", "rb") as test_image:
    encoded_file = base64.b64encode(test_image.read()).decode("utf-8")
    test_image.close()
    

attachedFile = Attachment(
    FileContent(encoded_file),
    FileName('attachment.png'),
    FileType('image/png'),
    Disposition('attachment')
)
message.attachment = attachedFile

try:
    sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)