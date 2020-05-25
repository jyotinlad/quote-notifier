from os import path
from json import load
from smtplib import SMTP_SSL


class Notifier:

    def __init__(self):
        credentials = self._get_credentials()
        user = credentials.get("user")
        password = credentials.get("password")

        self.server = SMTP_SSL('smtp.gmail.com', 465)
        self.server.ehlo()
        self.server.login(user, password)

    @staticmethod
    def _get_credentials():
        filename = "credentials.priv.json"
        if not path.isfile(filename):
            raise FileNotFoundError(filename)

        with open(filename, "r") as fh:
            return load(fh)

    def send(self, email, subject, body):
        message = f'Subject: {subject}\n\n{body}'
        self.server.sendmail(email, email, message)
