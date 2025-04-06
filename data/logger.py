# logger.py
# Logs sensor readings to data/logs/sensor_log.csv

import csv
import os
import time
import random  # Replace with real sensor reads
from datetime import datetime

LOG_DIR = "data/logs"
LOG_FILE = os.path.join(LOG_DIR, "sensor_log.csv")

def read_all():
    return {
        "temperature": round(20 + random.random() * 5, 2),
        "humidity": round(40 + random.random() * 10, 2),
        "moisture": round(300 + random.random() * 100, 2),
        "light": round(200 + random.random() * 400, 2),
        "ph": round(6.0 + random.random(), 2)
    }

def log_data():
    os.makedirs(LOG_DIR, exist_ok=True)

    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "temperature", "humidity", "moisture", "light", "ph"])

        data = read_all()
        writer.writerow([datetime.now().isoformat()] + list(data.values()))
        print(f"Logged: {data}")

if __name__ == "__main__":
    while True:
        log_data()
        time.sleep(30)  # log every 30 seconds
