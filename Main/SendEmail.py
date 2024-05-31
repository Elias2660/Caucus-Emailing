import os
from email.message import EmailMessage
import dotenv
from smtplib import SMTP_SSL as SMTP
from email.utils import formatdate
import sys
import CreateBarcode as CreateBarcode
import attachFile as attachFile
dotenv.load_dotenv("../local.env")

def send_email(recipients: list, session: int, name: str) -> str:
    SMTPserver = os.getenv("SMTPserver")
    sender = os.getenv("sender")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

    if not SMTPserver or not sender or not USERNAME or not PASSWORD:
        sys.exit("Missing environment variables")

    print(f"SMTP Server: {SMTPserver}")
    print(f"Sender: {sender}")
    print(f"Username: {USERNAME}")

    content = f"""
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
            <p style="padding-bottom: 10px;">Hi {name}!</p>
            <p style="padding-bottom: 10px;">We're excited to confirm your registration for Stuyvesant Junior Prom 2024, and we're looking forward to welcoming you to an unforgettable evening of fun. Below is your private barcode for entry to the event. Please ensure you save this email as this barcode will be scanned for your admission.</p>
            <p style="padding-bottom: 10px;">A follow-up email will be sent to you soon containing detailed information regarding the event. Until then!</p>
            <p>Cheers,<br>Elias, Will, and the Junior Caucus</p>
        </div>
    </div>
</body>
</html>"""

    subject = "Jprom Test"

    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = sender
        msg["Date"] = formatdate(localtime=True)
        msg["To"] = ", ".join(recipients)
        msg["List-Unsubscribe"] = (
            "<mailto:no-reply@junior.stuysu.org?subject=unsubscribe>"
        )

        msg.set_content(content, subtype="html")
        CreateBarcode.createBarcode(session, "barcode_image.png")
        attachFile.attach_file(msg, "barcode_image.png")
        conn = SMTP(SMTPserver)
        conn.set_debuglevel(True)  # Enable debugging output
        conn.login(USERNAME, PASSWORD)
        try:
            conn.sendmail(sender, recipients, msg.as_string())
        finally:
            conn.quit()
        return "Mail sent successfully"

    except Exception as e:
        print("Mail failed:", str(e))
        sys.exit(f"Mail failed; {str(e)}")


if __name__ == "__main__":
    print(send_email(["exu51@stuy.edu", "flam0799@gmail.com","esie50@stuy.edu"], 2083480230980, "Elias"))
    #     print(send_email(["esie50@stuy.edu"], 2083480230980, "Ethan"))
    #     print(send_email(["yzhang50@stuy.edu"], 2083480230980, "Will"))
