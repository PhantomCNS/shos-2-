# ====== imports ======
import socket
import utils
import wifi_storage


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

    if request.startswith("POST /save"):
        body = request.split("\r\n\r\n")[1]

        print("========== BODY ==========")
        print(body)

        # ====== gets password & ssid ======

        parts = body.split("&")
        print(parts)

        # ====== filter ssid & password ======
        ssid = parts[0].split("=")[1]
        password = parts[1].split("=")[1]

        # ===== save ssid & password ======
        wifi_storage.save_wifi_credentials(ssid, password)

    file = open("web/index.html", "r")
    html = file.read()
    file.close()

    response = """\
    HTTP/1.1 200 OK
    Content-Type: text/html

    """ + html

    client.send(response)
    client.close()