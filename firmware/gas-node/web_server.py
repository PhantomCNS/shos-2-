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

    request = client.recv(1024)
    print("Request:", request)

    file = open("web/index.html", "r")
    html = file.read()
    file.close()
    
    response = """\
    HTTP/1.1 200 OK
    Content-Type: text/html

    """ + html

    client.send(response)
    client.close()