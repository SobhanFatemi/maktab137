import logging

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

logger.addHandler(stream_handler)
logger.addHandler(file_handler)