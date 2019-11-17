import socket                   # Import socket module


# s = socket.socket()             # Create a socket object
host = socket.gethostbyname(socket.gethostname()) #10.6.34.166"  #Ip address that the TCPServer  is there
# port = 63342                     # Reserve a port for your service every new transfer wants a new port or you must wait.

# def check_connect(port):
#     print("initiate socket connection")
#     s.connect((host, port))
#     print("Connected")

def send(data, port):
    s = socket.socket()
    s.connect((host, port))
    s.send(data.encode())
    print("Sending through recreated socket")
    print('Sent ', repr(data.encode()))
    s.close()
