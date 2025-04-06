# light_sensor.py
# Reads light level (e.g. LDR)

def read_light():
    # TODO: Replace with real photodiode/LDR reading
    import random
    return round(100 + random.random() * 900, 2)

if __name__ == "__main__":
    print(f"Light Level: {read_light()} lx")
