# light_control.py
# Automatically turns on grow light if ambient light is low

import time
import random  # Replace with real light sensor
import RPi.GPIO as GPIO

LIGHT_PIN = 24  # GPIO pin for grow light relay
LIGHT_THRESHOLD = 300  # lux threshold

GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_PIN, GPIO.OUT)

def read_light():
    # TODO: Replace with real LDR or light sensor
    return round(100 + random.random() * 900, 2)

def control_light():
    lux = read_light()
    print(f"Ambient Light: {lux} lx")

    if lux < LIGHT_THRESHOLD:
        print("Low light detected. Turning on grow light.")
        GPIO.output(LIGHT_PIN, GPIO.HIGH)
    else:
        print("Sufficient light. Turning off grow light.")
        GPIO.output(LIGHT_PIN, GPIO.LOW)

if __name__ == "__main__":
    try:
        control_light()
    finally:
        GPIO.cleanup()

