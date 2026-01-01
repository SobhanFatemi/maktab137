import logging
<<<<<<< HEAD
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
=======

def add_filename_for_warnings(record):
    if record.levelno >= logging.ERROR:
        record.msg = f"{record.filename}:{record.lineno} - {record.msg}"
    return True

logger = logging.getLogger('UserActivityLogger')
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)
stream_formatter = logging.Formatter('%(message)s')
stream_handler.setFormatter(stream_formatter)

file_handler = logging.FileHandler('activity.log')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(file_formatter)

file_handler.addFilter(add_filename_for_warnings)
>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b

logger.addHandler(stream_handler)
logger.addHandler(file_handler)