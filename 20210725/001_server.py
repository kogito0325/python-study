# server

import socket
from typing import Tuple

# IP
HOST = 'localhost'  # 127.0.0.1
PORT = 8888  # 1024 ~ 65535

s = socket.socket()

s.bind((HOST, PORT))
s.listen()
print(f'Server open on {HOST}:{PORT}')

conn: socket.socket
addr: Tuple[str, int]

conn, addr = s.accept()

message = input()
conn.send(message.encode())
print(f'message has sent. > {message}')

conn.close()
print("Connection ended.")

s.close()
print('Server ended.')
