import socket
import io

class Connection():

    #Socket variables
    def __init__(self, address, port):
        self._address = address
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connect socket
    def connect(self):
         #Host socket and then wait for socket to close to host another
        try:
            self._socket.connect((self._address, self._port))
            print("Socket connected!")
        except:
            print("Service not running.")

    def recieveData(self):
        #Send the final file over socket(Likely back to user)
        file = self._socket.recv(1024)

        #Create local file after receiving and write bytes to it
        openFile = open("recievedBank.csv", "wb")
        openFile.write(file)
        print("File recieved!")
        
    def sendData(self, data):
        #Send the final file over socket(Likely back to user)
        self._socket.send(data.encode())
        print("Data sent!")