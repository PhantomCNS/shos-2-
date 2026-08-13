from machine import Pin
import time
import config
import connect
import wifi_storage
import wifi_setup
import buzzer
#import dht
import BlynkMan
import utils

# ===== checking wifi credentials =====
ssid, password = wifi_storage.load_wifi_credentials()
utils.debug_print("Loaded WiFi credentials: SSID={}, Password={}".format(ssid, password))

# ==== if ssid is None, then start AP mode =====
connected = False
if ssid is None or password is None:
    utils.debug_print("No WiFi credentials found. Starting AP mode for setup.")
    wifi_setup.start_ap_mode()
else:
    utils.debug_print("WiFi credentials found. Attempting to connect to WiFi.")

    connected = connect.ensure_connection()

    if not connected:
        utils.debug_print("WiFi connection failed. Starting AP mode for setup.")
        wifi_setup.start_ap_mode()

# dht_sensor = dht.DHT22(config.DHT_SENSOR)

# ===== Mute Buzzer function =====
muted = False  # Global variable to track buzzer state
def H_Mute_ON(pin):
    global muted
    muted = True
    utils.debug_print("Is Buzzer Muted? {}".format(str(muted)))

def H_Mute_OFF(pin):
    global muted
    muted = False
    utils.debug_print("Is Buzzer Muted? {}".format(str(muted)))
# btn IRQ
config.ON_BTN.irq(trigger = Pin.IRQ_FALLING, handler = H_Mute_ON)
config.OFF_BTN.irq(trigger = Pin.IRQ_FALLING, handler = H_Mute_OFF)

# ===== Mute buzzer function in Blynk =====
def mute_buzzer(value):
    global muted
    utils.debug_print("Buzzer state changed to: " + str(value[0]))
    
    if value[0] == "1":
        muted = True
    else:
        muted = False


# ===== Play alert if buzzer is allowed =====
def buzzer_allowed():
    if not muted:
        buzzer.play_gas_alert(cycles=2)


if connected:
    print("Successfully Connected!!!")

if connected and connect.blynk and not hasattr(connect.blynk, "_registered"):
    connect.blynk.on(config.SWITCH_IN_VPIN)(mute_buzzer)
    connect.blynk._registered = True

# ===== Alarm Status =====
alarm_sent = False


# ===== ges detection and dealing with it =====
def deal_with_gas(gas_value):
    global gas_state, alarm_sent
    if gas_value > config.gas_threshold:
        config.red_LED.on()
        buzzer_allowed()
        utils.debug_print("Gas leak detected, buzzer activated")
        config.RELAY.on()
        gas_state = "!!GAS LEAK DETECTED!!"
    else:
        config.red_LED.off()
        buzzer.stop_buzzer()
        config.RELAY.off()
        gas_state = "Gas levels normal"
        alarm_sent = False

    utils.debug_print("Gas Sensor Value: " + str(gas_state))
    utils.debug_print("Relay State: " + str(config.RELAY.value()))

# ===== Main Loop =====
while True:

    utils.debug_print("Entered Main Loop")

# ===== Read Sensors =====
    gas_value = config.GAS_SENSOR.read()
    utils.debug_print("Gas value = " + str(gas_value))

    # dht_sensor.measure()
    # dht_temp = dht_sensor.temperature()
    # dht_humidity = dht_sensor.humidity()

# ===== Actions =====
    deal_with_gas(gas_value)
    

# ===== start connection and its code =====
    if connected:
        try:
            connect.blynk.run()

            if not alarm_sent:
                if connect.blynk:
                    if gas_value > config.gas_threshold:
                        connect.blynk.log_event(
                            "gas_leak",
                            "Gas leak detected in kitchen"
                        )
                        alarm_sent = True

            BlynkMan.send_gas(gas_state)
            BlynkMan.send_gas_value(gas_value)
            # BlynkMan.send_humidity(dht_humidity)
            # BlynkMan.send_temperature(dht_temp)
            # BlynkMan.send_relay(fan_state)

        except Exception as e:
            print("Blynk Lost:", e)
            connect.blynk = None        
    time.sleep(1) 