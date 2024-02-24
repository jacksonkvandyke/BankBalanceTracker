import connectionClass
import testConnection
from threading import Thread
import json
import csv
import os
import time

#Service class
class Service():

    def __init__(self, address, port):
        self._address = address
        self._port = port
        self._connection = None

    def startService(self):
        #Create the awaiting socket on new thread
        self._connection = connectionClass.Connection(self._address, self._port, self)
        hostThread = Thread(target=self._connection.hostConnection)
        hostThread.start()

        time.sleep(2)

        #Create test socket
        test = testConnection.Connection("127.0.0.1", 50000)
        test.connect()

        #Send test file
        sendTest(test)
        test.recieveData()
    
    #Data manipulation functions
    def createCSVFile(self, data):
        #Create variables for read and write
        fields = ["Date", "Amount", "Change"]
        rows = []

        #Create the CSV file to create/update from the JSON data
        try:
            csvRead = open("bankData.csv", "r")

            #Get all previous information from CSV file
            csvReader = csv.reader(csvRead)

            #Get all rows
            for row in csvReader:
                rows.append(row) 

            #Set fields to empty so duplicate fields arent added to the file
            fields = []
        
        except:
            print("No CSV file present")

        #Create new CSV file
        csvWrite = open("bankData.csv", "a")

        #Add new information to previous CSV information
        jsonFile = json.loads(data)

        #Get change from last row
        change = 0
        if len(rows) > 2:
            change = jsonFile["amount"] - int(rows[len(rows) - 2][1])

        #Write data to new CSV file
        csvWriter = csv.writer(csvWrite)
        if len(fields) > 0: csvWriter.writerow(fields)
        csvWriter.writerow([jsonFile["date"], jsonFile["amount"], change])

        #Close file
        csvWrite.close()

        #Tell service to send complete file
        self._connection.sendData()
        
def sendTest(socket):
    #Test JSON
    testJson = '{ "date": "02/19/24", "amount": 750 }'

    #Send test file
    socket.sendData(testJson)

#Create and start service
service = Service("127.0.0.1", 50000)
service.startService()