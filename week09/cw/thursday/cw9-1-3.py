from abc import ABC, abstractmethod
import csv
import json

class DataProcessor(ABC):
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def __enter__(self):
        self.data = open(self.filepath, "r", encoding="utf-8")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.data:
            self.data.close()

    def run(self):
        self.process_data()

    @abstractmethod
    def process_data(self):
        pass


class CSVProcessor(DataProcessor):
    def process_data(self):
        reader = csv.reader(self.data)
        for row in reader:
            print(row)


class jsonProcessor(DataProcessor):
    def process_data(self):
        data = json.load(self.data)
        print(data)

#usage
if __name__ == "__main__":
    try:
        with CSVProcessor("data.csv") as file:
            file.run()
        with jsonProcessor("data.json") as file:
            file.run()
    except Exception as e:
        print(e)
