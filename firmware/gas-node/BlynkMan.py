from machine import Pin
import time
import BlynkLib
import config
import buzzer
import connect


def send_gas(value):
    connect.blynk.virtual_write(config.GAS_SENSOR_VPIN, value)

def send_temperature(value):
    connect.blynk.virtual_write(config.DHT_TEMP_VPIN, value)

def send_humidity(value):
    connect.blynk.virtual_write(config.DHT_HUM_VPIN, value)

def send_relay(value):
    connect.blynk.virtual_write(config.RELAY_VPIN, value)

def send_gas_value(value):
    connect.blynk.virtual_write(config.GAS_VALUE, value)

