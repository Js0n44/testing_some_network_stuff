import socket, json, random

id = random.randint(1, 10000)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

data = [
    {"message" : "hello there", "id" : id}
]

# Bind to IP and port
server_socket.bind(('localhost', 12345))

# Listen for connections (queue up to 5 connections)
server_socket.listen(5)
print("Server is listening on port 12345...")

# Accept a connection
client_socket, addr = server_socket.accept()
print(f"Connection from {addr} has been established.")

# Receive and send data
data = client_socket.recv(1024).decode()
print("Received from client:", data)
data = json.dumps(data)
client_socket.send(data.encode())

# Close connection
client_socket.close()
server_socket.close()
