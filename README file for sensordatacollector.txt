README for sensordatacollector

Overview

This script is designed to connect to a specific Bluetooth LE device and retrieve sensor data at a regular interval. 
The data includes measurements like temperature, humidity, light, UV index, and more. The script continuously scans for the target Bluetooth device, 
connects to it, fetches the latest sensor readings, and then stores them in a CSV file.

Dependencies:
bluepy
time
struct
csv


To install the bluepy library: 

pip install bluepy


How it Works:

The ScanDelegate class is responsible for scanning and connecting to the target device, retrieving the sensor data, parsing it, and then storing the parsed data in a CSV file.
The device's specific GATT characteristics are accessed using their UUIDs.
Data retrieved from the device is packed in bytes, and it's parsed using the struct module to extract and convert each sensor reading.
Parsed sensor data is written to a CSV file with a timestamp.


Configuration:
The hardcoded target device address is E0:4D:73:C7:BD:E9. If you need to connect to a different device, modify the target_device_address variable.
Data is saved in data.csv. If you wish to use another filename, modify the csv_file variable.
The default measurement interval is set to 1 minute (60 seconds). You can change this by updating the measurement_interval variable.

Usage:
To run the script, simply execute:

sudo python3 sensordatacollector.py

Output:
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

Known Issues and Limitations:
The device address is hardcoded. The script will only work with the specified device until it is edited.
Errors, such as connection issues, are handled with simple retry mechanisms. Depending on the environment, further refinements may be needed.
Always ensure the Bluetooth device is within range to improve the reliability of data retrieval.
The code only run on Virtual Machine Ubuntu 64 bit, assurance of it working on windows is not gauranteed. 

