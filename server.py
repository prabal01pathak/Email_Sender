import socket 
import select
import time

HEADER_LENGTH = 10
IP = '127.0.0.1'
PORT = 1234

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR , 1)
server.bind((IP,PORT))
server.listen()
sockets = [server]
clients = {}
print(f'Listioning connections on {IP}:{PORT}')
def recive_message(client_socket):
    try:
        message_header = client_sockets.recv(HEADER_LENGTH) 
        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8'))

        return f"{'header':message_header,'data':client_sockets.recv(message_length)'}"
    except:
        return False
while True:
    read_sockets , _ , exception_sockets = select.select(sockets,[],sockets)
    for notified_sockets in read_sockets:
        if notified_sockets == server:
            conn , addr = server.accept()
            user = recive_message(conn)
            if user is  False:
                continue
            sockets.append(user)
            clients[conn] = user
            print(f'accepted connection form {conn} ')

        else:
            message = recive_message(notified_sockets)
            if message is False:
                print('connection closed')
                sockets.remove(nofified_sockets)
                del clients[notified_sockets]
                continue
            user = clients[notified_sockets]
            print('recived message')

            for clients_sockets in clients:
                if clients_sockets != notified_sockets:
                    clients_sockets.send(user['data'])
        

        

