# #!/usr/bin/env python3

# import socket

# # AF_INET usa el protoolo iPv4
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

#     host = 'www.sina.com.cn'
#     port = 80

#     s.connect((host, port))
#     # s.sendall(b'Hello, world')
#     # data = s.recv(1024)
#     # Enviar datos:
#     s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# # print('Received', repr(data))
# # print(str(s.recv(4096), 'utf-8'))
#     # Recibir datos:
# buffer = []
# while True:
#  # Reciba hasta 1k bytes a la vez:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b".join(buffer)""
# # Cierre la conexión:
# s.close()

from socket import (
    socket, 
    AF_INET, 
    SOCK_STREAM,
    SO_REUSEADDR,
    SOL_SOCKET
)

#############################
# Variables
#############################
HOST, PORT = "127.0.0.1", 8080
request    = f"GET / HTTP/1.1\r\nHost: {HOST}:{PORT}\r\n\r\n".encode()
response   = "Hello word"  
#############################

with socket(AF_INET, SOCK_STREAM) as sock:
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.connect((HOST, PORT))
    # sending request
    sock.sendall(request)
    # receiving response
    while True:
        recv = sock.recv(1024)
        if recv == b'':
            break
        response += recv.decode()
    print(response)