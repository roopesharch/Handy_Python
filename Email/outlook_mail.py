import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')

# Email Sending Function
def send_email(subject: str, recipient: list, body: str, filenames_list=None):
    sender_email = "roop@outlook.com"
    smtp_server = "smtp.na.jnj.com"  # Replace with your SMTP server

    try:
        # Create the email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = ", ".join(recipient)
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        for f in filenames_list or []:
            with open(f, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=basename(f)
                )
            # After the file is closed
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            message.attach(part)

        # Connect and send the email
        server = smtplib.SMTP(smtp_server)
        server.default_port = 25
        server.send_message(message)
        server.quit()

        print("\nEmail sent successfully with the attached report.\n")
    except Exception as e:
        print(f"\nFailed to send email: {e}\n")

# Subject = "Trail mail"
# recipient = ['Max@gamil.com', 'Root@gmail.com']
# body = 'Hello Their'
# filenames_list = ['file_path1', 'file_path2']
# send_email(Subject, recipient, body, filenames_list)
