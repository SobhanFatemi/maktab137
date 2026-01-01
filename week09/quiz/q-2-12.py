import time
from datetime import datetime

class LogTime:
    def __enter__(self):
        self.start = datetime.now()
        print(f"Entered at: {self.start}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = datetime.now()
        print(f"Exited at:  {self.end}")

with LogTime():
    time.sleep(1.5)