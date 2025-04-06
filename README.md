Xenith GrowBox

Xenith GrowBox is a DIY, open-source automated plant growing system powered by a Raspberry Pi. It integrates real-time environmental sensing, smart control mechanisms, and camera vision to create a fully autonomous grow environment.

Built for hobbyists, researchers, and hackers who want to explore the intersection of nature and technology.


---

Features

Soil Monitoring: Humidity, temperature, and pH sensing

Light Monitoring: Light intensity sensor for adaptive illumination

Camera Integration: Real-time plant observation and time-lapse support

Automated Control:

Water pump activation based on moisture level

Grow light control based on light sensor

Ventilation triggers via servo/fan


Data Logging: Store readings and timestamps locally

Future AI Add-ons: Growth detection, anomaly spotting, and adaptive watering models



---

Hardware Requirements

Raspberry Pi (Pi 3, Pi 4, or Pi 5 recommended)

Pi Camera or USB webcam

Soil moisture sensor

Soil temperature sensor (e.g. DS18B20)

Analog pH sensor

Light intensity sensor (e.g. LDR or TSL2561)

Relay or transistor circuit for water pump

Optional: Grow light, fan/vent, 3D-printed case



---

Software Requirements

Python 3

GPIO Zero or RPi.GPIO

OpenCV (for camera functions)

Flask (optional dashboard)

SQLite or JSON for logging



---

Folder Structure

smart-grow-pi/
├── docs/                  # Setup guides, diagrams
├── hardware/              # Schematics, 3D models
├── sensors/               # Scripts for each sensor
├── automation/            # Control scripts for water, lights
├── camera/                # Capture + timelapse functions
├── data/logs/             # Stored sensor readings
└── dashboard/             # Web UI (optional)


---

License

MIT License


---

Credits

Built as an extension of the Xenith Protocol: a recursive symbiosis of intelligence, automation, and symbolic structure.


