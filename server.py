import socket
from  threading import Thread
import time
import os


from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
clients = {}
def handleClient():
    pass
def acceptConnections():
    global SERVER
    global clients

    while True:
        client , addr = SERVER.accept()
        
        client_name = client.recv(4096).decode().lower()
        #makin the dictionary
        clients[client_name] = {
                "client"         : client,
                "address"        : addr,
                "connected_with" : "",
                "file_name"      : "",
                "file_size"      : 4096
            }

        print(f"Connection established with {client_name} : {addr}")

        thread = Thread(target = handleClient, args=(client,client_name,))
        thread.start()


def setup():
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS , PORT))
    SERVER.listen(100)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

    acceptConnections()

def ftp():
    authorizer = DummyAuthorizer()
    authorizer.add_user("admin" , "admin" , "." , perm="elradfmw")
    handeler = FTPHandler
    handeler.authorizer = authorizer
    ftpServer = FTPServer((IP_ADDRESS , 21) , handeler)
    ftpServer.serve_forever() ## loop



setup_thread  = Thread(target=setup)
setup_thread.start()

ftp_thread = Thread(target=ftp)               
ftp_thread.start()