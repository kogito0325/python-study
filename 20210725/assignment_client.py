import socket
from time import sleep

HOST, PORT = 'sch.shtelo.org', 8888  # sch.shtelo.org:8888
running = True

while True:
    s = socket.socket()
    s.connect((HOST, PORT))
    print('client connected.')

    message = s.recv(1024).decode()
    print(f'{message}')

    s.send(str(int(message.split('+')[0]) + int(message.split('+')[1])).encode())
    s.close()
    print('client disconnected.\n')
    # sleep(1)
