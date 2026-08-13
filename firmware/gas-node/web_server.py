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

    try:
        client, address = server.accept()

    except OSError:
        # Nobody connected.
        return

    print("Client connected:", address)

    try:

        client.settimeout(1)

        request = client.recv(1024).decode()

        print(request)

        # Handle request...

    except Exception as e:

        print("HTTP error:", e)

    finally:

        client.close()

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

