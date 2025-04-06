# temp_sensor.py
# Reads temperature sensor (e.g. DS18B20)

def read_temperature():
    # TODO: Replace with actual 1-wire sensor reading
    import random
    return round(22 + random.random() * 5, 2)

if __name__ == "__main__":
    print(f"Temperature: {read_temperature()} °C")

