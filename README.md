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
The sensordatacollector.py script connects to a Bluetooth LE device to fetch sensor data like temperature, humidity, and more, storing the results in a CSV file. Dependencies include bluepy, csv, and struct. Additional instructions have been included in the file to help understanding of the data collection software. 

- Known Issues and Limitations:
  
The device address is hardcoded. The script will only work with the specified device until it is edited.
Errors, such as connection issues, are handled with simple retry mechanisms. Depending on the environment, further refinements may be needed.
Always ensure the Bluetooth device is within range to improve the reliability of data retrieval.
The code only run on Virtual Machine Ubuntu 64 bit, assurance of it working on windows is not gauranteed. 


