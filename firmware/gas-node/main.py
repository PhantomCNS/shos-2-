from machine import Pin
import time
from config import GAS_SENSOR, DHT_SENSOR, RELAY, LED, BLYNK_TEMPLATE_ID, blynk_auth_token, WiFi_SSID, WiFi_PASSWORD
from buzzer import play_gas_alert, stop_buzzer
import network
import dht 
import BlynkLib


dht_sensor = dht.DHT22(DHT_SENSOR)

# Initialize network and connect to WiFi
wlan = network.WLAN(network.STA_IF)
def connect_to_wifi(ssid, password):
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        time.sleep(1)
    print("Connected to WiFi:", wlan.ifconfig())

connect_to_wifi(WiFi_SSID, WiFi_PASSWORD)
# Initialize Blynk
blynk = BlynkLib.Blynk(blynk_auth_token,
    tmpl_id = BLYNK_TEMPLATE_ID,
    insecure = True
    )


# Main loop
while True:
    if not wlan.isconnected():
        connect_to_wifi(WiFi_SSID, WiFi_PASSWORD)
    # Read gas sensor value
    gas_value = GAS_SENSOR.value()
    
    # Read DHT sensor value 
    dht_sensor.measure()
    dht_temp = dht_sensor.temperature()  
    dht_humidity = dht_sensor.humidity() 

    # Control relay and alert pattern based on gas sensor value
    if gas_value == 0: 
        LED.on()
        play_gas_alert(cycles=2)
        stop_buzzer()
        RELAY.on()
        gas_state = "!!GAS LEAK DETECTED!!"

    else:
        LED.off()
        stop_buzzer()
        RELAY.off()
        gas_state = "Gas levels normal"
    
    # Print sensor values for debugging
    print("Gas Sensor Value:", gas_value)
    print("DHT Humidity Value:", dht_humidity)
    print("DHT Temperature Value:", dht_temp)

    # Send sensor values to Blynk
    blynk.run()  # Process Blynk events
    blynk.virtual_write(0, gas_state)  # Send gas sensor value to virtual pin V1
    blynk.virtual_write(1, dht_humidity)  # Send humidity value to virtual pin V2
    blynk.virtual_write(2, dht_temp)  # Send temperature value to virtual pin V3

    # Wait for a second before the next reading
    time.sleep(1)