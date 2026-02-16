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