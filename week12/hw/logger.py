import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

def add_filename_for_errors(record):
    if record.levelno >= logging.WARNING:
        record.msg = f"{record.filename}:{record.lineno} - {record.msg}"
    return True

logger = logging.getLogger("UserActivityLogger")
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter("%(message)s"))

file_handler = RotatingFileHandler("activity.log", maxBytes=100000, backupCount=5)
# file_handler = TimedRotatingFileHandler("activity.log", when="midnight", backupCount=7)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S"))
file_handler.addFilter(add_filename_for_errors)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)