import time
import struct
import csv
from bluepy.btle import Scanner, DefaultDelegate, Peripheral, BTLEDisconnectError

class ScanDelegate(DefaultDelegate):
    def __init__(self, csv_file):
        DefaultDelegate.__init__(self)
        self.csv_file = csv_file
        self.csv_writer = csv.writer(csv_file)
        self.last_seq_num = None

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if dev.addr.lower() == target_device_address.lower():
            print("Discovered target device:", dev.addr)
            self.retrieve_sensor_data(dev)

    def retrieve_sensor_data(self, dev):
        connected = False
        while not connected:
            try:
                # Connect to the device
                p = Peripheral(dev.addr, dev.addrType)
                connected = True

                # Access the Sensor Service
                sensor_service = p.getServiceByUUID("xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx")

                # Get the Latest data characteristic
                latest_data_char = sensor_service.getCharacteristics("xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx")[0]

                while True:
                    try:
                        # Read the data
                        data = latest_data_char.read()

                        # Parse the data
                        seq_num = struct.unpack("<B", data[0:1])[0]
                        if seq_num != self.last_seq_num:
                            self.parse_sensor_data(data)
                            self.last_seq_num = seq_num

                    except Exception as e:
                        print("Error:", e)
                        break

                    time.sleep(1)  # Delay between data retrievals

                # Disconnect from the device
                p.disconnect()

            except BTLEDisconnectError:
                print("Device disconnected")
                time.sleep(2)  # Delay before retrying connection

    def parse_sensor_data(self, data):
        # Extract and convert data according to the sensor's documentation
        seq_num = struct.unpack("<B", data[0:1])[0]
        temperature = struct.unpack("<h", data[1:3])[0] / 100.0
        humidity = struct.unpack("<h", data[3:5])[0] / 100.0
        light = struct.unpack("<H", data[5:7])[0]
        uv_index = struct.unpack("<H", data[7:9])[0] / 100.0
        pressure = struct.unpack("<H", data[9:11])[0] / 10.0
        noise = struct.unpack("<H", data[11:13])[0] / 100.0
        discomfort_index = struct.unpack("<h", data[13:15])[0] / 100.0
        heatstroke = struct.unpack("<h", data[15:17])[0] / 100.0
        battery_voltage = struct.unpack("<H", data[17:19])[0]

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        row = [timestamp, seq_num, temperature, humidity, light, uv_index, pressure, noise, discomfort_index, heatstroke, battery_voltage]
        self.csv_writer.writerow(row)
        self.csv_file.flush()  # Flush the file to save the data immediately

        print(f"Timestamp: {timestamp}, Seq Num: {seq_num}, Temperature: {temperature} °C, Humidity: {humidity} %, Light: {light} lx, UV Index: {uv_index}, Pressure: {pressure} hPa, Noise: {noise} dB, Discomfort Index: {discomfort_index}, Heatstroke: {heatstroke} °C, Battery Voltage: {battery_voltage} mV")

def write_header(csv_writer):
    header = ["Timestamp", "Seq Num", "Temperature (°C)", "Humidity (%)", "Light (lx)", "UV Index", "Pressure (hPa)", "Noise (dB)", "Discomfort Index", "Heatstroke (°C)", "Battery Voltage (mV)"]
    csv_writer.writerow(header)

# Hardcoded device address
target_device_address = "xx:xx:xx:xx:xx:xx"

csv_file = open("data.csv", "a", newline="")
csv_writer = csv.writer(csv_file)
delegate = ScanDelegate(csv_file)

measurement_interval = 60  # Set the measurement interval to 1 minute (60 seconds)

scanner = Scanner().withDelegate(delegate)

try:
    while True:
        try:
            print("Scanning for target device...")
            scanner.scan(3.0)  # Scan for a shorter period of time
        except Exception as e:
            print("Error:", e)
            print("Sleeping for 10 seconds before retrying...")
            time.sleep(10)

        # Add a delay before reconnecting to the peripheral device
        time.sleep(2)

except KeyboardInterrupt:
    print("Operation stopped by user")

finally:
    csv_file.close()

