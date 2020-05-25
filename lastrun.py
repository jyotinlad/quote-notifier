from datetime import datetime
from json import dump, load
from os import path


class LastRun:

    def __init__(self):
        self._last_run_file = "last_run.json"
        if path.isfile(self._last_run_file):
            with open(self._last_run_file, "r") as fh:
                data = load(fh)
                self.timestamp = datetime.strptime(data.get("last_run"), "%Y%m%d %H:%M:%S")
        else:
            self.timestamp = datetime.utcnow()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self._last_run_file, "w") as fh:
            dump({"last_run": self.timestamp.strftime("%Y%m%d %H:%M:%S")}, fh)
