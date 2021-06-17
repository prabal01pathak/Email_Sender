import socket
host = "127.0.0.1"
port = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((host,port))
    s.send(b'Hello User')
    data = s.recv(24)

print('Recived',repr(data))
