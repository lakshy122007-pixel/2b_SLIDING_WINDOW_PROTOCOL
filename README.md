# 2b IMPLEMENTATION OF SLIDING WINDOW PROTOCOL
## AIM
To implement client–server data transmission using Python sockets with framing and ACK.
## ALGORITHM:
1. Start the server and wait for a client connection.
2. Client inputs frame size and data to be transmitted.
3. Split data into frames based on the given frame size.
4. Send frames to the server; server receives each frame and replies with ACK.
5. Send STOP signal and terminate both client and server.

## PROGRAM
```
Server:
import socket
server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server started. Waiting for client...")
conn, addr = server.accept()
print("Connected from", addr)

while True:
    frame = conn.recv(1024).decode()
    if frame == "STOP":
        print("Stopping server...")
        break
    
    print("Received frame:", frame)
    conn.send("ACK".encode())

conn.close()
server.close()

Client:
import socket
client = socket.socket()
client.connect(("localhost", 5000))

size = int(input("Enter frame size: "))
data = input("Enter data to send: ")

frames = [data[i:i+size] for i in range(0, len(data), size)]

for frame in frames:
    print("Sending frame:", frame)
    client.send(frame.encode())
    
    ack = client.recv(1024).decode()
    print("Server response:", ack)

client.send("STOP".encode())
client.close()
print("Client stopped.")




```
## OUPUT
Server:
![alt text](<2.b server.png>)
Client:
![alt text](<2.b cli.png>)
## RESULT
Thus, python program to perform stop and wait protocol was successfully executed
