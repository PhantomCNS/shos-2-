from machine import Pin
import time
import dht
import network

# Pin Configurations
gas_sensor_pin = 21
dht_sensor_pin = 4
relay_pin = 18
Buzzer_pin = 19
LED_pin = 2
WiFi_SSID = "Your_WiFi_SSID"
WiFi_PASSWORD = "Your_WiFi_Password"

# Pin Objects
GAS_SENSOR = Pin(gas_sensor_pin, Pin.IN)
DHT_SENSOR = Pin(dht_sensor_pin, Pin.IN)
RELAY = Pin(relay_pin, Pin.OUT)
BUZZER = Pin(Buzzer_pin, Pin.OUT)
LED = Pin(LED_pin, Pin.OUT)