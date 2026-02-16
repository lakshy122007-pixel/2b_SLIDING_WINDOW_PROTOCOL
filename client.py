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