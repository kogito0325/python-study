import socket

HOST = 'localhost'  # 127.0.0.1
PORT = 8888  # 1024 ~ 65535
running = True

s = socket.socket()

s.connect((HOST, PORT))
print(f'Client connected to {HOST}:{PORT}')

while running:
    value = int(s.recv(1024).decode())
    if value > 1000000:
        break
    print(value)
    value = str(value + 1).encode()
    s.send(value)

s.close()
print('Client closed.')
