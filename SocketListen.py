import socket

s = socket.socket()
s.bind(("127.0.0.1", 6666))
s.listen(5)

while True:
    clt, address = s.accept()
    print("It worked")
