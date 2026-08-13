# ====== imports ======
import network 
import socket
import utils

# ====== start AP ======
ap = network.WLAN(network.AP_IF)

def start_ap_mode():    
    ap.active(True)
    ap.config(
        ssid='SHOS-Setup',
        password='gasnode123',
        authmode=network.AUTH_WPA_WPA2_PSK
        )
utils.debug_print("Access Point started with SSID: SHOS-Setup")

utils.debug_print("Access Point IP Address: {}".format(ap.ifconfig()[0]))
