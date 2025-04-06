# ph_sensor.py
# Reads pH sensor values (placeholder version)

def read_ph():
    # TODO: Replace with actual ADC value
    import random
    return round(6.5 + random.random() * 1.0, 2)

if __name__ == "__main__":
    print(f"pH Value: {read_ph()}")
