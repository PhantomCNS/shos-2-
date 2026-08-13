# ====== imports ======
import network 

# ====== start AP ======
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(
    ssid='SHOS-Setup',
    password='gasnode123'
    ) 