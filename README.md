# 2b IMPLEMENTATION OF SLIDING WINDOW PROTOCOL
## AIM
## ALGORITHM:
1. Start the program.
2. Get the frame size from the user
3. To create the frame based on the user request.
4. To send frames to server from the client side.
5. If your frames reach the server it will send ACK signal to client
6. Stop the Program
## PROGRAM
# client.py:
```
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
```
# server.py:
```
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
```
## OUPUT
![alt text](<Screenshot 2026-05-15 105435.png>)
![alt text](<Screenshot 2026-05-15 105421.png>)
## RESULT
Thus, python program to perform stop and wait protocol was successfully executed
