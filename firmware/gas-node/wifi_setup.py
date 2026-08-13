# ====== imports ======
import network
import utils
import web_server

ap = network.WLAN(network.AP_IF)

# ==== start AP mode function ======
def start_ap_mode():

    ap.active(True)

    ap.config(
        ssid="SHOS-Setup",
        password="gasnode123",
        authmode=network.AUTH_WPA_WPA2_PSK
    )

    utils.debug_print(
        "Access Point started with SSID: SHOS-Setup"
    )

    utils.debug_print(
        "Access Point IP Address: {}".format(
            ap.ifconfig()[0]
        )
    )

    web_server.start_server()