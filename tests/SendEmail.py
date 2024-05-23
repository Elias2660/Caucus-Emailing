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
import CreateBarcode


def sendEmail(
    sender: str, sendee: str, name: str, code: int, attachment_name="ticket.png"
) -> None:

    dotenv.load_dotenv("../local.env")

    message = Mail(
        from_email=sender,
        to_emails=sendee,
        subject="Jprom Test",
        html_content=f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="jcaucus.css">
</head>
<body>
    <div class="text">
        <div class="greeting">
            Hi {name}, 
     
        </div>
               <br>
        <div>
            We're excited to confirm your registration for Stuyvesant Junior Prom 2024. We look forward to welcoming you to an unforgettable evening of fun.
            Below is your private barcode for entry to the event. Please ensure you save this email as this barcode will be scanned for your admission. 
        </div>
        <br>
        <div>

        </div>
        <div class="second-last">
            A follow-up email will be sent to you soon containing detailed information regarding the event. Until then!
        </div>
        <div>
            <br>
            Cheers, <br>The Junior Caucus
        </div>
    </div>
</body>
</html>""",
    )

    CreateBarcode.createBarcode(code, f"{attachment_name}")

    with open(f"{attachment_name}", "rb") as test_image:
        encoded_file = base64.b64encode(test_image.read()).decode("utf-8")
        test_image.close()

    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName(f"{attachment_name}"),
        FileType("image/png"),
        Disposition("attachment"),
    )
    message.attachment = attachedFile

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(response.status_code)
        print("message should be sent correctly")
    except Exception as e:
        print(e.message)


if __name__ == "__main__":
    sendEmail("flam0799@gmail.com", "yzhang50@stuy.edu", "Will", 2083480230980)
