# Smart Home IoT System

## Tech Stack
- Flask
- Python
- React
- TypeScript
- InfluxDB
- MQTT
- Grafana
- Raspberry PI

## Description
This project is a smart-home IoT system developed by a team of two students as part of their engineering software course during the 2023/2024 academic year. The system integrates multiple Raspberry PI devices connected to sensors and actuators, designed to monitor and control various elements of a smart home. The system includes real-time data transmission using MQTT, storage in an InfluxDB database, and visualization using Grafana. A web-based interface built with React and TypeScript allows users to interact with the smart home devices, monitor sensor data, and manage alarms.

## System Overview
The smart-home system contains three Raspberry PI devices, each connected to various sensors and actuators. Key components include door sensors, PIR motion detectors, temperature and humidity sensors, ultrasonic sensors, LED lights, buzzers, and more. The system manages real and simulated devices, providing alarm functionalities, sensor data visualization, and control over the system's status.

### Devices Overview
- **PI1**: Door sensors, ultrasonic sensor, PIR motion sensor, door light, and buzzer.
- **PI2**: Garage sensors (temperature, humidity, motion, gyro), LCD display.
- **PI3**: Bedroom sensors (PIR, temperature, humidity), RGB light, 7-segment display, buzzer.


## How to Run
### Prerequisites
#### InfluxBb
To start InfluxDB, navigate to the folder where your installation is located (if you didn’t change the default path during installation, it should be `C:\Program Files\InfluxData\influxdb`) and run the following command:
```bash
./influxd
```
or simply:
```bash
influxd
```

#### MQTT (Mosquitto Broker)
To start the Mosquitto MQTT broker, navigate to the folder where your installation is located (if you didn’t change the default path during installation, it should be C:\Program Files\mosquitto) and run the following command:

```bash
./mosquitto
```
or simply:
```bash
mosquitto
```

#### Grafana
To set up and run Grafana for visualizing the sensor data:

1. Install Grafana from the [official website](https://grafana.com/) if you haven’t already.
2. After installation, simply start it by running the following command:
```bash
grafana-server
```
3. Once Grafana is running, open a browser and go to http://localhost:3000.
4. Login using the default credentials (admin/admin) and configure a new data source connected to InfluxDB for viewing sensor data on customizable dashboards.

### The project
1. Clone the repository.
2. Navigate to the `backend` directory and set up the Python Flask server:
   ```bash
   pip install -r requirements.txt
   flask run
   ```
3. In the frontend directory, run the React application:
    ```bash
    npm install
    npm run dev
    ```
4. Navigate to the `iot_device_handler` folder to run the device handler for both real and simulated IoT devices:
    ```bash
    python main.py
    ```
5. Access the web application at http://localhost:5173 in your browser.

**Note**: Ensure that the Raspberry PI devices and connected sensors/actuators (or simulations) are set up.
