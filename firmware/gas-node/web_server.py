# ====== imports ======
import socket
import utils


server = socket.socket()
server.bind(('0.0.0.0', 80))
server.listen(1)
print("HTTP server ready on port 80")

# ====== While loop ======
while True:
    client, address = server.accept()
    print("Client connected from:", address)
    client.close()