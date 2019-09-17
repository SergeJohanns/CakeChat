import socket

s = socket.socket()
#s.bind(("127.0.0.1", 6666))
s.connect(("127.0.0.1", 6666))
