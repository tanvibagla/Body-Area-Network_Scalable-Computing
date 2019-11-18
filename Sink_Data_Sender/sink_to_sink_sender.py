import socket
import tqdm
import os

SEPARATOR = " "
BUFFER_SIZE = 4096 # send 4096 bytes each time step

host = '10.6.34.166'
port = 58575

filename = '../Receiver/Pacemaker_Data.json'

filesize = os.path.getsize(filename)
print(filesize)

#create client socket
s = socket.socket()

#connecting to the server
print("[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")

# send the filename and filesize

print(filename+SEPARATOR+str(filesize))
s.send(filename+SEPARATOR+str(filesize).encode())


progress = tqdm.tqdm(range(filesize), "Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    print("file: ", f)
    for _ in progress:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
# close the socket
s.close()











# import socket                   # Import socket module
# import os
#
# path = '../Receiver/'
# files = []
# # r = root, d = directories, f = files
# for r, d, f in os.walk('../Receiver/'):
#     for file in f:
#         print(type(file))
#         if '.json' in file:
#             files.append(os.path.join(r, file))
#
# print(files)
# host = socket.gethostbyname(socket.gethostname()) #10.6.34.166"  #Ip address that the TCPServer  is there
# port = 61117
#
# def send():
#     s = socket.socket()
#     # s.connect((host, port))
#     for file in files:
#         print(type(file))
#         s.send(file.encode())
#     print("Sending through recreated socket")
#     print('Sent ', repr(file.encode()))
#     s.close()
#
#
# send()