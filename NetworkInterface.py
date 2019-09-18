import socket as socketLib
import threading
import time

standardPort = 6666 #TODO: Change port number to something outside of semi reserved range

class Interface:
    def __init__(self, port):
        self.listenIP = ""
        self.port = port
        self.buffer = 1024
        self.inSocket = socketLib.socket()
        self.outSocket = socketLib.socket()
    def Listen(self, reciever):
        #Takes in a recieving class with a method MessageIn that takes in any recieved messages and handles them
        self.inSocket.bind((self.listenIP, self.port))
        self.inSocket.listen(self.buffer)
        clt, address = self.inSocket.accept()
        while True:
            reciever.MessageIn(clt.recv(self.buffer))
    def Connect(self, ip):
        self.outSocket.connect((ip, self.port))

def BuildTunnel(ip, reciever):
    try:
        listen = threading.Thread(target = interface.Listen, args = (reciever,))
        connect = threading.Thread(target = interface.Connect, args = (ip,))
        listen.start()
        connect.start()
    except Exception as e:
        print(e)
        print("Couldn't build connection. Try again or contact your system administrator if the problem persists.")

def Send(message):
    interface.outSocket.send(message)

interface = Interface(standardPort) #Create main instance of network interface

#DEBUG
"""
class Reciever:
    def MessageIn(message):
        print(message)
BuildTunnel("192.168.43.155", Reciever())
"""
