from logging import DEBUG

from machine import Pin
import time
from config import GAS_SENSOR, DHT_SENSOR, RELAY, LED, BLYNK_TEMPLATE_ID, blynk_auth_token, WiFi_SSID, WiFi_PASSWORD
from buzzer import play_gas_alert, stop_buzzer, mute_buzzer, muted, buzzer_allowed
import network
import dht 
import BlynkLib
from BlynkMan import send_gas, send_temperature, send_humidity, send_relay, blynk
from utils import debug_print

dht_sensor = dht.DHT22(DHT_SENSOR)



# Initialize network and connect to WiFi
wlan = network.WLAN(network.STA_IF)
def connect_to_wifi(ssid, password):
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        time.sleep(1)
    debug_print("Connected to WiFi:" + str(wlan.ifconfig()))

connect_to_wifi(WiFi_SSID, WiFi_PASSWORD)
# Initialize Blynk

alarm_sent = False
# Main loop
while True:

    if not wlan.isconnected():
        connect_to_wifi(WiFi_SSID, WiFi_PASSWORD)
        blynk = BlynkLib.Blynk(blynk_auth_token,
            tmpl_id = BLYNK_TEMPLATE_ID,
            insecure = True
            )

    # Read gas sensor value
    gas_value = GAS_SENSOR.value()
    # Read DHT sensor value 
    dht_sensor.measure()
    dht_temp = dht_sensor.temperature()  
    dht_humidity = dht_sensor.humidity() 

    blynk.run()  # Process Blynk events

    # Control relay and alert pattern based on gas sensor value
    if gas_value == 0:
        LED.on()
        buzzer_allowed()  # play gas alert if buzzer is allowed to sound
        debug_print("Gas leak detected, buzzer activated")
        RELAY.on()
        gas_state = "!!GAS LEAK DETECTED!!"

        if not alarm_sent:
            blynk.log_event("gas_leak", "Gas leak detected in kitchen")
            alarm_sent = True

    else:
        LED.off()
        stop_buzzer()
        RELAY.off()
        gas_state = "Gas levels normal"

        alarm_sent = False            

    # Print sensor values for debugging
    debug_print("Gas Sensor Value:" + str(gas_value))
    debug_print("DHT Humidity Value:" + str(dht_humidity))
    debug_print("DHT Temperature Value:" + str(dht_temp))


    # Send sensor values to Blynk
    send_humidity(dht_humidity)  # Send humidity value to virtual pin V2
    send_temperature(dht_temp)  # Send temperature value to virtual pin V3
    send_gas(gas_value)  # Send gas sensor value to virtual pin V1
    send_relay(RELAY.value())  # Send relay value to virtual pin V4

    # Wait for a second before the next reading
    time.sleep(1)