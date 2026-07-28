from utils import debug_print
from machine import PWM
from config import BUZZER
import config
import network
import dht
import time
from BlynkMan import blynk


buzzer_pwm = PWM(BUZZER)
buzzer_pwm.duty(0)  # Start silent until alert begins

# buzzer initialization
def buzz(duration=0.5, freq=1000):
    buzzer_pwm.freq(freq)
    buzzer_pwm.duty(512)  # Turn on buzzer
    time.sleep(duration)  # Wait for the specified duration
    buzzer_pwm.duty(0)  # Turn off buzzer

# Buzzer control functions
def play_gas_alert(cycles=3, first_freq=900, second_freq=1400, duration=0.4):
    for _ in range(cycles):
        buzz(duration, freq=first_freq)
        buzz(duration, freq=second_freq)
        time.sleep(0.3)  # Short pause between cycles

# Stop buzzer function
def stop_buzzer():
    buzzer_pwm.duty(0)  # Turn off buzzer

muted = True  # Global variable to track buzzer state

# Mute buzzer function
@blynk.on(config.SWITCH_IN_VPIN)
def mute_buzzer(value):
    global muted
    debug_print("Buzzer state changed to: " + str(value[0]))
    if value[0] == "1":
        muted = True
    else:
        muted = False

# Function to play gas alert if buzzer is allowed to sound
def buzzer_allowed():
    if not muted:
        play_gas_alert(cycles=2)