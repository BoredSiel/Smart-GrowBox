# moisture_sensor.py
# Reads soil moisture (analog)

def read_soil_moisture():
    # TODO: Replace with GPIO ADC input
    import random
    return round(300 + random.random() * 200, 2)

if __name__ == "__main__":
    print(f"Soil Moisture: {read_soil_moisture()}")
