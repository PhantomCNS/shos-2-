# libraries
import network 
import utils

# Initialization
ap = network.WLAN(network.AP_IF)

ap.active(True)

# Configeration
ap.config(
    essidv = "SHOS_Setup",
    password = "Neoro_Anatomy",
    authmode = network.AUTH_WPA_WPA2_PSK
)

if utils.DEBUG:
    utils.debug_print(ap.ifconfig())