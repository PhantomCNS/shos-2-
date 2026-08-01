from machine import Pin
import time
import config
import connect
import buzzer
#import dht 
import BlynkLib
import BlynkMan 
import utils

dht_sensor = dht.DHT22(config.DHT_SENSOR)


# Initialize network and connect to WiFi

muted = False  # Global variable to track buzzer state

# Mute buzzer function
@connect.blynk.on(config.SWITCH_IN_VPIN)
def mute_buzzer(value):
    global muted
    utils.debug_print("Buzzer state changed to: " + str(value[0]))
    if value[0] == "1":
        muted = True
    else:
        muted = False


# Function to play gas alert if buzzer is allowed to sound
def buzzer_allowed():
    if not muted:
        buzzer.play_gas_alert(cycles=2)


alarm_sent = False
# Main loop
while True:
    config.LED.value(0)
    global gas_state

    if not connect.wlan.isconnected():
       blynk = connect.connect_everything()  # Reconnect to WiFi and Blynk if disconnected

    # Read gas sensor value
    gas_value = config.GAS_SENSOR.value()

    #################################
    # Read DHT sensor value 
    #dht_sensor.measure()
    #dht_temp = dht_sensor.temperature()  
    #dht_humidity = dht_sensor.humidity() 
    #################################
    connect.blynk.run()  # Process Blynk events

    # Control relay and alert pattern based on gas sensor value & humidity threshold
    if gas_value == 0:
        config.LED.on()
        buzzer_allowed()  # play gas alert if buzzer is allowed to sound
        utils.debug_print("Gas leak detected, buzzer activated")
        config.RELAY.on()
        gas_state = "!!GAS LEAK DETECTED!!"

        if not alarm_sent:
            connect.blynk.log_event("gas_leak", "Gas leak detected in kitchen")
            alarm_sent = True
    #################################

    #elif dht_humidity > config.dht_humidity_threshold:
    #    config.RELAY.on()
    #    utils.debug_print("Humidity threshold exceeded, fan activated")
    #################################

    else:
        config.LED.off()
        buzzer.stop_buzzer()
        config.RELAY.off()
        gas_state = "Gas levels normal"

        alarm_sent = False            

        

    if config.fan.value() == 1 and config.RELAY.value() == 1:
        fan_state = "Fan is OFF"
        BlynkMan.send_relay(0)  # Send relay value to virtual pin V4
    else:
        fan_state = "Fan is ON"
        BlynkMan.send_relay(1)  # Send relay value to virtual pin V4

    # Print sensor values for debugging
    utils.debug_print("Gas Sensor Value:" + str(gas_state))

    #################################
    #utils.debug_print("DHT Humidity Value:" + str(dht_humidity))
    #utils.debug_print("DHT Temperature Value:" + str(dht_temp))
    #################################

    utils.debug_print("Relay State:" + str(config.RELAY.value()))
    utils.debug_print("Fan State:" + str(fan_state))


    # Send sensor values to Blynk

    #################################
    #BlynkMan.send_humidity(dht_humidity)  # Send humidity value to virtual pin V2
    #BlynkMan.send_temperature(dht_temp)  # Send temperature value to virtual pin V3
    #################################

    BlynkMan.send_gas(gas_state)  # Send gas sensor value to virtual pin V1
    BlynkMan.send_relay(fan_state)  # Send relay value to virtual pin V4

    # Wait for a second before the next reading
    time.sleep(1)