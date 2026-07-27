from machine import Pin
import time
from config import GAS_SENSOR, DHT_SENSOR, RELAY, LED
from buzzer import play_gas_alert, stop_buzzer
import network
import dht 


dht_sensor = dht.DHT22(DHT_SENSOR)


while True:
    stop_buzzer()  # Ensure buzzer is off at startup

    # Read gas sensor value
    gas_value = GAS_SENSOR.value()
    
    # Read DHT sensor value 
    dht_sensor.measure()
    dht_value = dht_sensor.temperature()  
    dht_humidity = dht_sensor.humidity() 

    # Control relay and alert pattern based on gas sensor value
    if gas_value == 0: 
        LED.on()
        play_gas_alert(cycles=2)
        stop_buzzer()
        RELAY.on()

    else:
        LED.off()
        stop_buzzer()
        RELAY.off()
    
    # Print sensor values for debugging
    print("Gas Sensor Value:", gas_value)
    print("DHT Humidity Value:", dht_humidity)
    print("DHT Temperature Value:", dht_value)
    
    # Wait for a second before the next reading
    time.sleep(1)