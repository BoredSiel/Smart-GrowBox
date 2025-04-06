# water_control.py
# Automatically waters plants if soil is too dry

import time
import random  # Replace with real sensor import
import RPi.GPIO as GPIO

PUMP_PIN = 23  # GPIO pin for water pump relay
MOISTURE_THRESHOLD = 400  # Adjust this threshold as needed

GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMP_PIN, GPIO.OUT)

def read_soil_moisture():
    # TODO: Replace with real sensor code
    return round(300 + random.random() * 200, 2)

def control_water():
    soil_moisture = read_soil_moisture()
    print(f"Soil Moisture: {soil_moisture}")

    if soil_moisture < MOISTURE_THRESHOLD:
        print("Soil too dry. Activating pump.")
        GPIO.output(PUMP_PIN, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(PUMP_PIN, GPIO.LOW)
    else:
        print("Soil moisture sufficient. No watering.")

if __name__ == "__main__":
    try:
        control_water()
    finally:
        GPIO.cleanup()
