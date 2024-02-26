# IndoorOutdoor-Wearable-Sensor-Privacy
## Privacy-preserving approach to Indoor/Outdoor Detection with a Wearable Environmental Sensor

### Table of Contents
1. Overview
2. Project Components
    - Sensor Data Collector
    - Data Analysis
    - Model Training
    - Dataset Description
3. Usage
4. Known Issues and Limitations
5. License
6. Contact Information

## 1. Overview

The main aim of this project is to use a privacy-preserving approach to automatically detect whether someone is indoors or outdoors using an OMRON 2JCIE-BL01 wearable sensor, employing machine learning techniques. This comprehensive effort involves collecting, analysing, and predicting sensor data to distinguish between indoor and outdoor environments. It combines a Python script for data collection via Bluetooth LE devices, Jupyter notebooks for preprocessing and analysis, a model training notebook, and a supportive dataset. This approach is particularly beneficial for sectors like healthcare, where it can aid in elderly care, monitoring dementia patients, mental health care, and child monitoring.

## 2. Project Components
### Sensor Data Collector
The sensordatacollector.py script connects to a Bluetooth LE device to fetch sensor data like temperature, humidity, and more, storing the results in a CSV file. Dependencies include bluepy, csv, and struct. The details are as follows

- How it Works:

The ScanDelegate class is responsible for scanning and connecting to the target device, retrieving the sensor data, parsing it, and then storing the parsed data in a CSV file.
The device's specific GATT characteristics are accessed using their UUIDs.
Data retrieved from the device is packed in bytes, and it's parsed using the struct module to extract and convert each sensor reading.
Parsed sensor data is written to a CSV file with a timestamp.


- Configuration:

The hardcoded target device address is xx:xx:xx:xx:xx:xx. If you need to connect to a different device, modify the target_device_address variable.
Data is saved in data.csv. If you wish to use another filename, modify the csv_file variable.
The default measurement interval is set to 1 minute (60 seconds). You can change this by updating the measurement_interval variable.

- Usage:

To run the script, simply execute:

sudo python3 sensordatacollector.py

- Output:

The script will display messages when:
Scanning for the target device.
Successfully discovering the target device.
Reading data.
Encountering errors.

The CSV file will be updated with the following columns:

Timestamp
Sequence Number
Temperature (°C)
Humidity (%)
Light (lx)
UV Index
Pressure (hPa)
Noise (dB)
Discomfort Index
Heatstroke (°C)
Battery Voltage (mV)

The script will run indefinitely, scanning and logging data, until interrupted by the user (using Ctrl + C).

- Known Issues and Limitations:

The device address is hardcoded. The script will only work with the specified device until it is edited.
Errors, such as connection issues, are handled with simple retry mechanisms. Depending on the environment, further refinements may be needed.
Always ensure the Bluetooth device is within range to improve the reliability of data retrieval.
The code only run on Virtual Machine Ubuntu 64 bit, assurance of it working on windows is not gauranteed. 

