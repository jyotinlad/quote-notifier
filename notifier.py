from dotenv import load_dotenv
from os import getenv
from smtplib import SMTP_SSL


class Notifier:

    def __init__(self):
        load_dotenv()
        user = getenv("GMAIL_USER")
        password = getenv("GMAIL_PASSWORD")

        self.server = SMTP_SSL('smtp.gmail.com', 465)
        self.server.ehlo()
        self.server.login(user, password)

    def send(self, email, subject, body):
        message = f'Subject: {subject}\n\n{body}'
        self.server.sendmail(email, email, message)
