File: read_sensors.py

Description: Reads data from sensors (temp, humidity, soil moisture, light, pH)

import time import random  # Replace with actual GPIO reads

def read_temperature(): return round(20 + random.random() * 10, 2)

def read_humidity(): return round(40 + random.random() * 20, 2)

def read_soil_moisture(): return round(300 + random.random() * 100, 2)

def read_light(): return round(200 + random.random() * 500, 2)

def read_ph(): return round(6.0 + random.random(), 2)

if name == "main": while True: temp = read_temperature() humidity = read_humidity() soil = read_soil_moisture() light = read_light() ph = read_ph()

print(f"Temp: {temp}°C | Humidity: {humidity}% | Soil: {soil} | Light: {light}lx | pH: {ph}")
    time.sleep(5)

