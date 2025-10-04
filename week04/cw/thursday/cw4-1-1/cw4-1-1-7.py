log_data = """
INFO: Starting process...
DEBUG: Connecting to database.
ERROR: Connecting timeout.
INFO: Process finished.
ERROR: File not found.
"""

def read_lines(data):
    for line in data.strip().split('\n'):
        yield line

def filter_errors(lines_gen):
    for line in lines_gen:
        if "ERROR" in line:
            yield line

def extract_message(errors_gen):
    for line in errors_gen:
        extracted_msg = line.replace("ERROR: ", "")
        yield extracted_msg

log_lines = read_lines(log_data)
error_lines = filter_errors(log_lines)
error_messages = extract_message(error_lines)

for msg in error_messages:
    print(msg)