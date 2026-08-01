from machine import Pin
import time
import config
import connect
import buzzer
#import dht
import BlynkLib
import BlynkMan
import utils

# dht_sensor = dht.DHT22(config.DHT_SENSOR)


muted = False  # Global variable to track buzzer state


# Mute buzzer function
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

# Initialize network and connect to WiFi
if connect.ensure_connection():
    if not hasattr(connect.blynk, "_registered"):
        connect.blynk.on(config.SWITCH_IN_VPIN)(mute_buzzer)
        connect.blynk._registered = True
else:
    print("No connection")

if connect.wlan.isconnected():
    print("Successfully Connected!!!")

alarm_sent = False

# Main loop
while True:
    utils.debug_print("Entered Main Loop")

    gas_value = config.GAS_SENSOR.value()
    utils.debug_print("Gas value = " + str(gas_value))

    # dht_sensor.measure()
    # dht_temp = dht_sensor.temperature()
    # dht_humidity = dht_sensor.humidity()

    connect.ensure_connection()

    if connect.blynk:
        connect.blynk.run()

    if gas_value == 0:
        config.LED.on()
        buzzer_allowed()
        utils.debug_print("Gas leak detected, buzzer activated")
        config.RELAY.on()
        gas_state = "!!GAS LEAK DETECTED!!"

        if not alarm_sent:
            if connect.blynk:
                connect.blynk.log_event(
                    "gas_leak",
                    "Gas leak detected in kitchen"
                )
                alarm_sent = True

    else:
        config.LED.off()
        buzzer.stop_buzzer()
        config.RELAY.off()
        gas_state = "Gas levels normal"
        alarm_sent = False

    utils.debug_print("Gas Sensor Value: " + str(gas_state))
    utils.debug_print("Relay State: " + str(config.RELAY.value()))

    # BlynkMan.send_humidity(dht_humidity)
    # BlynkMan.send_temperature(dht_temp)

    BlynkMan.send_gas(gas_state)
    # BlynkMan.send_relay(fan_state)

    time.sleep(1)