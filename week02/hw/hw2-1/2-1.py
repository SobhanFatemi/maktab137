import csv
import json

class WrongFormat(Exception):
    "Format is wrong!"

log_path = "Home Work/2/1/server.log"
try:
    def log_to_list(log_path):
        line_list = []
        with open(log_path, "r") as log:
            for line in log:
                line_list.append(line)
        return line_list

    def read_log(log_path):
        with open(log_path, "r") as log:
            for line in log:
                print(line.strip())

    read_log(log_path)

    lines: list = log_to_list(log_path)

    with open('Home Work/2/1/critical_errors.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Message"])

    counter = 1
    error_counter = 0
    notice_counter = 0
    unidentified_level = 0
    for line in lines:
        try:
            if line[0] == "[" and line[25] == "]" and line[27] == "[":
                timestamp = line[1:25]
                if line[33] == "]":
                    level = "error"
                    message = line[35:-1]
                elif line[34] == "]":
                    level = "notice"
                    message = line[36:-1]
            else:
                raise WrongFormat()
            
            if level == "error":
                with open('Home Work/2/1/critical_errors.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([timestamp, message])
                error_counter += 1
            elif level == "notice":
                notice_counter += 1
                
        except WrongFormat:
            with open('Home Work/2/1/errors.log', 'a') as file:
                file.write(f"{counter}: {line}")
            unidentified_level += 1
        counter += 1
            


    summary = {
        "Notice": notice_counter,
        "Error": error_counter,
        "Unidentified": unidentified_level
    }

    with open('Home Work/2/1/summary.json', 'w', encoding='utf-8') as file:
        json.dump(summary, file, ensure_ascii=False, indent=4)

except FileNotFoundError:
    print("Server log file not found!")