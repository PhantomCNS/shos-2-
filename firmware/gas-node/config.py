from machine import Pin
import time
import dht
import network
#define BLYNK_TEMPLATE_ID "TMPL2663gkE68"
#define BLYNK_TEMPLATE_NAME "SHOS 1"
#define BLYNK_AUTH_TOKEN "PtZuWfyPnv1tC9UJH8jtw85UmL-z9QTG"

# Pin Configurations
gas_sensor_pin = 21
dht_sensor_pin = 4
relay_pin = 18
Buzzer_pin = 19
LED_pin = 2
BLYNK_TEMPLATE_ID = "TMPL2663gkE68"
blynk_auth_token = "PtZuWfyPnv1tC9UJH8jtw85UmL-z9QTG"
WiFi_SSID = "Wokwi-GUEST"
WiFi_PASSWORD = ""

# Pin Objects
GAS_SENSOR = Pin(gas_sensor_pin, Pin.IN)
DHT_SENSOR = Pin(dht_sensor_pin, Pin.IN)
RELAY = Pin(relay_pin, Pin.OUT)
BUZZER = Pin(Buzzer_pin, Pin.OUT)
LED = Pin(LED_pin, Pin.OUT)

# BLYNK Configuration
GAS_SENSOR_VPIN = 0
DHT_TEMP_VPIN = 1
DHT_HUM_VPIN = 2
RELAY_VPIN = 3
SWITCH_IN_VPIN = "V4"