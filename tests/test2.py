import os
import dotenv
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail,
    Attachment,
    FileContent,
    FileName,
    FileType,
    Disposition,
)

with open("Content.html", "r") as file:
    data = file.read()

with open("stuy.webp", "rb") as topAttatchment:
    stuy_logo = base64.b64encode(topAttatchment.read())
    

print(stuy_logo)
dotenv.load_dotenv("../local.env")


message = Mail(
    from_email=os.getenv("SEND_EMAIL"),
    to_emails=os.getenv("SEND_EMAIL"),
    subject="JProm Test 1",
    html_content=f"""
    <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="display: grid; color: #4054B9; font-family: 'forma-djr-text', sans-serif; font-weight: bold;">
    <img class="stuy" src="data:image/jpeg;base64,{stuy_logo}" alt="stuy" style="padding-top: 8vh; padding-bottom: 10vh; height: 10vh; justify-self: center;">
    <div class="text" style="padding-left: 5vw; padding-right: 5vw;">
        <div class="greeting" style="padding-bottom: 1vh;">
            Hi Elias, 
        </div>
        <div>
            We're excited to confirm your registration for Stuyvesant Junior Prom 2024. We look forward to welcoming you to an unforgettable evening of fun.
            Below is your private barcode for entry to the event. Please ensure you save this email as this barcode will be scanned for your admission. 
        </div>
        <div>

        </div>
        <div class="second-last" style="padding-bottom: 8vh;">
            A follow-up email will be sent to you soon containing detailed information regarding the event. Until then!
        </div>
        <div>
            Cheers, <br>The Junior Caucus
        </div>
    </div>
</body>
</html>
    """,
)


try:
    sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
    response = sg.send(message)
except Exception as e:
    print(e.message)
else:
    print("Message sent sucessfully")
