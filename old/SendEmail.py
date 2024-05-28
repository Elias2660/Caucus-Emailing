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
import Main.CreateBarcode as CreateBarcode


def sendEmail(
    sender: str, sendee: str, name: str, code: int, attachment_name="ticket.png"
) -> None:

    dotenv.load_dotenv("local.env")

    message = Mail(
        from_email=sender,
        to_emails=sendee,
        subject="Jprom Test",
        html_content=f"""<html>
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
            <p style="padding-bottom: 10px;">Hi {name}!</p>
            <p style="padding-bottom: 10px;">We're excited to confirm your registration for Stuyvesant Junior Prom 2024, and we're looking forward to welcoming you to an unforgettable evening of fun. Below is your private barcode for entry to the event. Please ensure you save this email as this barcode will be scanned for your admission.</p>
            <p style="padding-bottom: 10px;">A follow-up email will be sent to you soon containing detailed information regarding the event. Until then!</p>
            <p>Cheers,<br>Elias, Will, and the Junior Caucus</p>
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
    sendEmail("flam0799@gmail.com", "exu51@stuy.edu", "Will", 2083480230980)
