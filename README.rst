Bank Balance Tracker README:

Request Data:

1. First start the microservice by running the python file "startService.py"
2. Now send a JSON file to the service based on the services port and address in the following format: '{ "date": "02/19/24", "amount": 750 }'. Change the date and value to your specific values.
3. Once the microservice has completed processing the file it will instantly start sending back the file

Example:

#Connect to service
    try:
        self._socket.connect((self._address, self._port))
        print("Socket connected!")
    except:
        print("Service not running.")
        
#Send JSON(NOTE: This will be called only if the socket successfully connects)
    testJson = '{ "date": "02/19/24", "amount": 750 }'
    self._socket.send(data.encode())


Recieve Data:

1. Recieve the data over the current socket connection, don't decode() the data since it is already in byte format.
2. Open a local file in write BYTE format to save the data recieved from the microservice. Example:

//Recieve data
file = self._socket.recv(1024)

//Create CSV file and write to in BYTE format
openFile = open("recievedBank.csv", "wb")

//Write to file
openFile.write(file)

3. You are done! The microservice has successfully tracked the current date and balance info in your bankCSV


NOTE 1: The microservice stores a local CSV file which is edited and sent back to the user.
NOTE 2: The microservice will continue to run in the background until stopped allowing the user to send as many request as desired to the service.
