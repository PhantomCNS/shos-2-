from machine import Pin
import time
import network
import config
import BlynkLib
import utils


wlan = network.WLAN(network.STA_IF)

def connect_to_wifi(ssid, password):
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        time.sleep(1)
    utils.debug_print("Connected to WiFi:" + str(wlan.ifconfig()))


connect_to_wifi(config.WiFi_SSID, config.WiFi_PASSWORD)

def connect_blynk():
    blynk = BlynkLib.Blynk(config.blynk_auth_token,
        tmpl_id = config.BLYNK_TEMPLATE_ID,
        insecure = True
        )
    return blynk
# The last issue solved
blynk = connect_blynk()

while not wlan.isconnected():
    connect_to_wifi()
    blynk = connect_blynk()