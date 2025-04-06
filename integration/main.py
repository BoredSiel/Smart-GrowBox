main.py

Master controller for the Smart GrowBox system

import time from sensors.temp_sensor import read_temperature from sensors.moisture_sensor import read_soil_moisture from sensors.ph_sensor import read_ph from sensors.light_sensor import read_light from automation.water_control import control_water from automation.light_control import control_light from data.logger import log_data

CYCLE_INTERVAL = 60  # seconds

def run_cycle(): print("\n--- New Cycle ---") try: temp = read_temperature() soil = read_soil_moisture() ph = read_ph() light = read_light()

print(f"Temp: {temp}°C | Soil: {soil} | pH: {ph} | Light: {light} lx")

    control_water()
    control_light()
    log_data()

except Exception as e:
    print(f"Error during cycle: {e}")

if name == "main": print("Smart GrowBox system started.") while True: run_cycle() time.sleep(CYCLE_INTERVAL)


