import utils
from machine import PWM
import config
import network
import dht
import time


buzzer_pwm = PWM(config.BUZZER)
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

