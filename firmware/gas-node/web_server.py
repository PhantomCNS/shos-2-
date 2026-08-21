# ====== imports ======
from machine import reset
import socket
import utils
import wifi_storage

server = None
# ==== handle requests ======
def handle_requests():

    global server

    if server is None:
        return

    # Check for a new client
    try:
        client, address = server.accept()

    except OSError:
        # Nobody connected
        return

    print("Client connected:", address)

    try:

        client.settimeout(0.5)

        request = client.recv(1024).decode()

        print("========== REQUEST ==========")
        print(request)

        # ====== GET / ======
        

        if request.startswith("GET / "):

            with open("web/index.html", "r") as file:
                html = file.read()

            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html; charset=UTF-8\r\n"
                "Content-Length: {}\r\n"
                "Connection: close\r\n"
                "\r\n"
                "{}"
            ).format(len(html), html)

            client.send(response.encode())

        # ====== POST /save ======


        elif request.startswith("POST /save"):

            body = request.split("\r\n\r\n", 1)[1]

            print("BODY:")
            print(body)

            parts = body.split("&")

            ssid = url_decode(
                parts[0].split("=", 1)[1]
            )

            password = url_decode(
                parts[1].split("=", 1)[1]
            )

            print("SSID:", ssid)
            print("Password:", password)

            wifi_storage.save_wifi_credentials(
                ssid,
                password
            )

            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n"
                "Connection: close\r\n"
                "\r\n"
                "<html>"
                "<body>"
                "<h1>WiFi credentials saved!</h1>"
                "<p>ESP32 is rebooting...</p>"
                "</body>"
                "</html>"
            )

            client.send(response.encode())

            client.close()
            
            print("Credentials saved. Rebooting...")
            reset()
    except Exception as e:

        print("HTTP error:", e)

    finally:

        try:
            client.close()
        except:
            pass



# ====== URL Decode function ======
def url_decode(text):
    text = text.replace("+", " ")

    result = ""
    i = 0

    while i < len(text):

        if text[i] == "%" and i + 2 < len(text):

            hex_value = text[i + 1:i + 3]
            result += chr(int(hex_value, 16))
            i += 3

        else:
            result += text[i]
            i += 1

    return result

def start_server():
    global server
    server = socket.socket()
    server.setblocking(False)
    server.bind(('0.0.0.0', 80))
    server.listen(1)
    print("HTTP server ready on port 80")

