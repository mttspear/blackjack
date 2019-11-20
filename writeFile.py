import csv
import os

class WriteFile(object):
    
    def createFile(self, headers):
        open("log.csv", 'w').close()
        with open(r'log.csv', 'a') as f:
            writer = csv.writer(f, delimiter=',', lineterminator='\n')
            writer.writerow(headers)
    
    def logData(self, array):  
        with open(r'log.csv', 'a') as f:
            writer = csv.writer(f, delimiter=',', lineterminator='\n')
            writer.writerow(array)