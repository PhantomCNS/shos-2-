import time
from machine import PWM
from config import BUZZER

buzzer_pwm = PWM(BUZZER)
buzzer_pwm.duty(0)  # Start silent until alert begins

def buzz(duration=0.5, freq=1000):
    buzzer_pwm.freq(freq)
    buzzer_pwm.duty(512)  # Turn on buzzer
    time.sleep(duration)  # Wait for the specified duration
    buzzer_pwm.duty(0)  # Turn off buzzer


def play_gas_alert(cycles=3, first_freq=900, second_freq=1400, duration=0.4, pause=0.3):
    for _ in range(cycles):
        buzz(duration, freq=first_freq)
        time.sleep(pause)
        buzz(duration, freq=second_freq)
        time.sleep(pause)


def stop_buzzer():
    buzzer_pwm.duty(0)  # Turn off buzzer
