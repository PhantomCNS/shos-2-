from machine import Pin, time_ticks_ms, time_ticks_diff
import time
from config import GAS_SENSOR, DHT_SENSOR, RELAY, LED
from buzzer import play_gas_alert, stop_buzzer

while True:
    # Read gas sensor value
    gas_value = GAS_SENSOR.value()
    
    # Read DHT sensor value (assuming you have a function to read it)
    dht_value = DHT_SENSOR.value()  # Replace with actual reading method
    
    # Control relay and alert pattern based on gas sensor value
    if gas_value == 1:  # Example threshold
        RELAY.on()
        LED.on()
        play_gas_alert(cycles=2)
        stop_buzzer()
    else:
        RELAY.off()
        LED.off()
        stop_buzzer()
    
    # Print sensor values for debugging
    print("Gas Sensor Value:", gas_value)
    print("DHT Sensor Value:", dht_value)
    
    # Wait for a second before the next reading
    time.sleep(1)