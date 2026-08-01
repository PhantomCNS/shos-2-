import utils
from machine import Pin
import config
import network
#import dht
import time


buzzer_pwm = Pin(config.BUZZER)

# buzzer initialization
def buzz(duration=0.5):
    buzzer_pwm.value(1)
    time.sleep(duration)  # Wait for the specified duration
    buzzer_pwm.value(0)  # Turn off buzzer

# Buzzer control functions
def play_gas_alert(cycles=3, duration=0.4):
    for _ in range(cycles):
        buzz(duration)
        time.sleep(0.2)          # Short pause between cycles        

        buzz(duration)
        time.sleep(0.5)          # Short pause between cycles        


# Stop buzzer function
def stop_buzzer():
    buzzer_pwm.value(0)  # Turn off buzzer

