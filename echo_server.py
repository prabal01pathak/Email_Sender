import socket

host = '127.0.0.1'
port = 65432
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen(4)
    conn,addr = s.accept()
    with conn:
        print('connected by ',addr)
        msg = ''
        while True:
            data = conn.recv(24)
            if len(data)<=0:
                break
            conn.send(bytes('Welcome to the server',encoding= 'utf-8'))
