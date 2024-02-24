import socket
import time
import io

class Connection():

    #Socket variables
    def __init__(self, address, port, service):
        self._address = address
        self._port = port
        self._service = service
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._connectedSocket = socket.socket()
        self._connected = False

    #Host socket
    def hostConnection(self):
         #Host socket and then wait for socket to close to host another
         while True:
            try:
                self._socket.bind((self._address, self._port))
                self._socket.listen(1)
                print(f"Socket waiting on port: ", self._port)
            except:
                print("Service still running.")
                #Wait for one second to stop thread from using too many resources
                time.sleep(1)

            #Check if socket is already connected and if so recieve data constantly
            if self._connected == False:
                connectedInfo = self._socket.accept()
                self._connectedSocket = connectedInfo[0]
                self._connected = True

            if self._connected == True:
                self.recieveData()

    def recieveData(self):
        #Read data from socket
        data = self._connectedSocket.recv(1024).decode()

        #Create CSV file from data
        if len(data) != 0:
            self._service.createCSVFile(data)

    def sendData(self):
        #Send the final file over socket(Likely back to user)
        csv = open("bankData.csv", "rb")

        #Convert file to bytes array
        csvToBytes = csv.read()

        #Send bytes to reciever
        self._connectedSocket.send(csvToBytes)
        print("File sent!")
    

    