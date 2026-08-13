# ====== imports ======
import network 
import socket
import utils
# ====== start AP ======
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(
    ssid='SHOS-Setup',
    password='gasnode123'
    )
utils.debug_print("Access Point started with SSID: SHOS-Setup")

utils.debug_print("Access Point IP Address: {}".format(ap.ifconfig()[0]))
