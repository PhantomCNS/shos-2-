from machine import Pin
import time
import BlynkLib
from config import GAS_SENSOR, DHT_SENSOR, RELAY, LED, BLYNK_TEMPLATE_ID, blynk_auth_token, WiFi_SSID, WiFi_PASSWORD, GAS_SENSOR_VPIN, DHT_TEMP_VPIN, DHT_HUM_VPIN, RELAY_VPIN, SWITCH_IN_VPIN
from buzzer import mute_buzzer, play_gas_alert, stop_buzzer

blynk = BlynkLib.Blynk(blynk_auth_token,
    tmpl_id = BLYNK_TEMPLATE_ID,
    insecure = True
    )

@blynk.on("V4", mute_buzzer)  # Listen for virtual pin V4 changes to mute/unmute buzzer

blynk.run()

def send_gas(value):
    blynk.virtual_write(GAS_SENSOR_VPIN, value)

def send_temperature(value):
    blynk.virtual_write(DHT_TEMP_VPIN, value)

def send_humidity(value):
    blynk.virtual_write(DHT_HUM_VPIN, value)

def send_relay(value):
    blynk.virtual_write(RELAY_VPIN, value)

