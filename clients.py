import socket 
import errno
import select

HEADER_LENGTH = 10
IP = '127.0.0.1'
PORT = 1234
username = input('username:')
server_conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_conn.connect((IP,PORT))
server_conn.setblocking(False)
user_name = username.encode('utf-8')
user_header = f"{len(user_name):<{HEADER_LENGTH}}".encode('utf-8')
server_conn.send(user_header+user_name)


