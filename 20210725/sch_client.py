import socket

HOST = 'sch.shtelo.org'  # 175.115.211.24
PORT = 8888  # 1024 ~ 65535

s = socket.socket()

s.connect((HOST, PORT))
print(f'Client connected to {HOST}:{PORT}')

message = s.recv(1024).decode()
print(f'{HOST}:{PORT} > {message}')

s.close()
print('Client closed.')
