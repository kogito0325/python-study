import socket

HOST = 'localhost'  # 127.0.0.1
PORT = 8888  # 1024 ~ 65535
running = True

s = socket.socket()

s.bind((HOST, PORT))
s.listen()
print(f'Server open on {HOST}:{PORT}')

conn, addr = s.accept()

conn.send('1'.encode())

while running:
    value = int(conn.recv(1024).decode())
    value = str(value + 1).encode()
    conn.send(value)

conn.close()
print("Connection ended.")

s.close()
print('Server ended.')
