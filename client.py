import socket

s = socket.socket()

host = 'localhost'
port = 12345

s.connect((host, port))

while True:

    data = s.recv(1024).decode()

    if not data:
        break

    print("Received:", data)

    ack = "ACK"
    s.send(ack.encode())

s.close()