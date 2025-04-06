# temp_humidity.py
# Reads temperature and humidity from DHT11/DHT22 sensor

import Adafruit_DHT

# Set sensor type and GPIO pin
SENSOR = Adafruit_DHT.DHT22  # or Adafruit_DHT.DHT11
PIN = 4  # GPIO pin where the sensor is connected

def read_temp_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    if humidity is not None and temperature is not None:
        return round(temperature, 2), round(humidity, 2)
    else:
        return None, None

if __name__ == "__main__":
    temp, hum = read_temp_humidity()
    if temp is not None:
        print(f"Temperature: {temp}°C | Humidity: {hum}%")
    else:
        print("Failed to retrieve data from DHT sensor.")
