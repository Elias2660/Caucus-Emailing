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
        html_content=f"""<html>
    <head>
      <meta charset="UTF-8">
      <title>JProm Ticket</title>
    </head>
    <body style="font-family: 'Helvetica Neue', sans-serif; color: #0629B0; margin: 0; padding: 0; background-color: #FFFEF9;">
      <div style="max-width: 500px; margin: 0 auto; padding: 50px;">
        <div style="text-align: center; margin-bottom: 50px;">
          <img src="https://github.com/Junior-Caucus-SU/TicketCatcher/blob/main/stuy_logo.png?raw=true" alt="Stuy Icon" style="max-width: 100px;">
        </div>
        <div style="text-align: left; line-height: 1.2;">
          <p style="font-size: larger;">Hi {name}!,</p>
          <p style="font-size: larger;">We're excited to confirm your registration for Stuyvesant Junior Prom 2024. We look forward to welcoming you to an unforgettable evening of fun. Below is your private barcode for entry to the event. Please ensure you save this email as this barcode will be scanned for your admission.</p>
          //REPLACE WITH BARCODE
          <p style="margin-top: 40px; font-size: larger;">A follow-up email will be sent to you soon containing detailed information regarding the event. Until then!</p>
          <div style="margin-top: 40px;">
            <p style="font-size: larger;">Cheers,<br>Elias, Will, and the Junior Caucus</p>
          </div>
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
