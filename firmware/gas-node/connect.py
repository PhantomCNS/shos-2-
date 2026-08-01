import time
import network
import BlynkLib
import config
import utils

wlan = network.WLAN(network.STA_IF)
blynk = None


def connect_to_wifi():

    if wlan.isconnected():
        return True

    if not wlan.active():
        wlan.active(True)
    wlan.connect(config.WiFi_SSID, config.WiFi_PASSWORD)
    timeout = 10

    while timeout > 0:
        if wlan.isconnected():
            config.WIFI_LED.on()
            utils.debug_print(str(wlan.ifconfig()))
            return True

        time.sleep(1)
        timeout -= 1

    config.WIFI_LED.off()
    print("WiFi Failed")
    return False


def connect_blynk():
    global blynk

    try:
        print("Connecting to Blynk...")
        blynk = BlynkLib.Blynk(
            config.blynk_auth_token,
            tmpl_id=config.BLYNK_TEMPLATE_ID,
            insecure=True
        )
        print("Connected to Blynk!")
        return blynk

    except OSError:
        blynk = None
        print("Failed to connect to Blynk.")
        return False
    
def ensure_connection():
    global blynk

    if not wlan.isconnected():
        blynk = None
        if not connect_to_wifi():
            return False

    if blynk is None:
        blynk = connect_blynk()
        if blynk is False:
            return False
    return True
