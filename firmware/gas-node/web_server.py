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

    # ====== getting POST data ======
    request = client.recv(1024).decode()

    print("========== REQUEST ==========")
    print(request)

    body = request.split("\r\n\r\n")[1]

    print("========== BODY ==========")
    print(body)

    parts = body.split("&")
    print(parts)

    file = open("web/index.html", "r")
    html = file.read()
    file.close()

    response = """\
    HTTP/1.1 200 OK
    Content-Type: text/html

    """ + html

    client.send(response)
    client.close()