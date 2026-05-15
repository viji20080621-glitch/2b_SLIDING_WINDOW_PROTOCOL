import socket
import time

s = socket.socket()

host = 'localhost'
port = 12345

s.bind((host, port))
s.listen(1)

print("Waiting for connection...")

conn, addr = s.accept()
print("Connected by", addr)

frames = ["Frame 1", "Frame 2", "Frame 3", "Frame 4", "Frame 5"]

window_size = 3
i = 0

while i < len(frames):

    for j in range(i, min(i + window_size, len(frames))):
        print("Sending:", frames[j])
        conn.send(frames[j].encode())
        time.sleep(1)

    for j in range(i, min(i + window_size, len(frames))):
        ack = conn.recv(1024).decode()
        print("Received:", ack)

    i += window_size

conn.close()
s.close()