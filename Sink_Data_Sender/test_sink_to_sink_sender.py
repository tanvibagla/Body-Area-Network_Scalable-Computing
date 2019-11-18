import socket

s = socket.socket()
s.connect(("localhost",9999))
f = open ("../Receiver/Pacemaker_Data.json", "rb")
print('f: ', f)
l = f.read(1024)
while (l):
    print('l: ', l)
    s.send(l)
    l = f.read(1024)
s.close()