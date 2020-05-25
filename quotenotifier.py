from argparse import ArgumentParser
from datetime import datetime, timedelta
from json import load
from random import choice, shuffle
from time import sleep

from lastrun import LastRun
from notifier import Notifier


class QuoteNotifier:

    def __init__(self):
        self._notifier = Notifier()

    @staticmethod
    def _get_quotes():
        filename = "quotes.json"
        with open(filename, "r") as fh:
            return load(fh)

    def generate(self):
        quotes = self._get_quotes()
        shuffle(quotes)

        quote = choice(quotes)
        print(f"sending \"{quote}\"")

        email = "j.lad.uk@gmail.com"
        subject = "Daily Quote"
        self._notifier.send(email, subject, quote)

    def run(self, interval_mins):
        with LastRun() as lr:
            while True:
                last_run = lr.timestamp
                next_run = last_run + timedelta(minutes=interval_mins)

                now = datetime.utcnow()
                if now > next_run:
                    self.generate()
                    lr.timestamp = datetime.utcnow()

                sleep(10)


if __name__ == "__main__":
    parser = ArgumentParser(description="A process to send quotes via email.")
    parser.add_argument("-i", dest="interval", type=int, required=True, help="Interval Minutes")
    args = parser.parse_args()

    quote_notifier = QuoteNotifier()
    quote_notifier.run(args.interval)
