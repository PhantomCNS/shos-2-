from machine import Pin
import time
#import dht
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
check_pin = 4
fan_in_pin = 17
BLYNK_TEMPLATE_ID = "TMPL2663gkE68"
blynk_auth_token = "PtZuWfyPnv1tC9UJH8jtw85UmL-z9QTG"
WiFi_SSID = "Emy"
WiFi_PASSWORD = "Emy&Omar&Salma"
ON_BTN_Pin = 12
OFF_BTN_Pin = 13

# Pin Objects
GAS_SENSOR = Pin(gas_sensor_pin, Pin.IN)
DHT_SENSOR = Pin(dht_sensor_pin, Pin.IN)
RELAY = Pin(relay_pin, Pin.OUT)
BUZZER = Pin(Buzzer_pin, Pin.OUT)
red_LED = Pin(LED_pin, Pin.OUT)
check_led = Pin(check_pin, Pin.OUT)
fan = Pin(fan_in_pin, Pin.IN)
ON_BTN = Pin(ON_BTN_Pin, Pin.IN, Pin.PULL_UP)
OFF_BTN = Pin(OFF_BTN_Pin, Pin.IN, Pin.PULL_UP)

# BLYNK Configuration
GAS_SENSOR_VPIN = 0
DHT_TEMP_VPIN = 1
DHT_HUM_VPIN = 2
RELAY_VPIN = 5
SWITCH_IN_VPIN = "V4"

dht_humidity_threshold = 60  # Humidity threshold for fan activation