import json
import csv

def file_reader(file_path):
    try:
        with open(file_path, 'r') as file:

            ext = file_path.split('.')[-1].lower()

            if ext == "json":
                reader = json.load(file)
                return reader
            elif ext == "csv":
                file.seek(0)
                csv_list = []
                reader = csv.reader(file)
                for line in reader:
                    csv_list.append(line)
                return csv_list
            elif ext == "txt":
                file.seek(0)
                lines = file.read()
                return lines
    except FileNotFoundError:
        return f"'{file_path}' was not found!"

            
print(file_reader("cw-2-9.json")) 
print(file_reader("cw2-2-9.json"))
print(file_reader("cw2-2-7.csv"))
print(file_reader("lorem.txt"))
