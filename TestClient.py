import NetworkInterface
import time

class Reciever:
    def MessageIn(self, message):
        print(message)

NetworkInterface.BuildTunnel(input("Target IP: "), Reciever())
while True:
    time.sleep(1)
    NetworkInterface.Send(b"Whatever")
