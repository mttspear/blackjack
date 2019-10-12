import csv
import os

class WriteFile(object):
    
    def createFile(self, headers):
        open("C:/Users/Matt/blackjack/log.csv", 'w').close()
        with open(r'C:/Users/Matt/blackjack/log.csv', 'a') as f:
            writer = csv.writer(f, delimiter=',', lineterminator='\n')
            writer.writerow(headers)
    
    def logData(self, array):  
        with open(r'C:/Users/Matt/blackjack/log.csv', 'a') as f:
            writer = csv.writer(f, delimiter=',', lineterminator='\n')
            writer.writerow(array)