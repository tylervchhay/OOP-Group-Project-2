import csv

#Class for CSV Reader
class CSVreader_service:
    def __init__(self):
        pass
    #Method for opening file and converting to dic
    def read_file(self, file_name):
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
            