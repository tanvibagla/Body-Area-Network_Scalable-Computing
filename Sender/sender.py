import socket

host = socket.gethostbyname(socket.gethostname()) #10.6.34.166"  #Ip address that the TCPServer  is there

def send(data, port):
    s = socket.socket()
    s.connect((host, port))
    s.send(data.encode())
    print("Sending through recreated socket")
    print('Sent ', repr(data.encode()))
    s.close()
