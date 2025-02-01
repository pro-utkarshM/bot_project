# Wandering Robot Powered by Deepseek

This project involves a robot that autonomously moves around based on sensor input, powered by Deepseek, which runs on a laptop. The robot has a Raspberry Pi 5 (RPI), a Raspberry Pi Camera, and an ultrasonic sensor for distance measurement. The laptop processes the data from the Raspberry Pi and sends back commands for the robot to execute.

## **Project Structure**

```
robot_project/
│
├── laptop/
│   ├── app.py                # Flask API running on the laptop
│   └── Deepseek_query.py        # Code to query Deepseek model
│
├── robot/
│   ├── main.py               # Main control code for the robot on Raspberry Pi
│   ├── camera.py             # Code to capture image from Pi Camera
│   └── ultrasonic.py         # Code to read ultrasonic sensor
│
└── shared/
    └── config.py             # Configuration settings (e.g., laptop IP)
```

---

## **Installation**

### **1. Laptop Setup (Flask API)**

#### Prerequisites:
- Python 3.7 or later
- Deepseek installed via Ollama
- Install Flask:
  ```bash
  pip install flask
  ```

#### Steps:
1. Clone the repository or download the project files to your laptop.
2. Ensure Deepseek is correctly set up on your laptop using Ollama. You can run it by using the following command:
   ```bash
   ollama run deepseek-r1:1.5b "your query here"
   ```
3. Run the Flask app on your laptop:
   ```bash
   python laptop/app.py
   ```
   The Flask API will be available on the local network (e.g., `http://192.168.137.235:5000`).

### **2. Raspberry Pi Setup**

#### Prerequisites:
- Raspberry Pi 5
- Pi Camera
- Ultrasonic sensor (e.g., HC-SR04)
- Python 3
- Install required libraries:
  ```bash
  sudo apt-get install python3-requests python3-picamera2
  pip install requests
  ```

#### Steps:
1. Clone the repository or download the project files to your Raspberry Pi.
2. Update the `laptop_ip` in `shared/config.py` to match your laptop’s local IP address (`192.168.137.235`).
3. Run the robot control program:
   ```bash
   python robot/main.py
   ```

---

## **How It Works**

1. **Raspberry Pi Sensors:**
   - The Raspberry Pi reads data from the ultrasonic sensor to measure the distance to the nearest object.
   - The Raspberry Pi Camera captures an image of the surroundings.

2. **Communication:**
   - The Raspberry Pi sends the sensor data (distance and image) to the Flask API running on the laptop via HTTP POST requests.
   
3. **Deepseek Processing:**
   - The Flask API processes the data and queries Deepseek using the sensor information (e.g., distance).
   - Deepseek responds with a command (e.g., "move forward," "turn left," etc.).

4. **Robot Action:**
   - The Raspberry Pi receives the command and controls the robot’s movement accordingly.

---

## **File Descriptions**

### **Laptop Side**
- **`laptop/app.py`**: Runs a Flask API that listens for sensor data from the Raspberry Pi and sends back movement commands based on Deepseek's response.
- **`laptop/Deepseek_query.py`**: Queries the Deepseek model using the data from the Raspberry Pi and returns a command.

### **Robot Side**
- **`robot/main.py`**: Main control program for the robot. It sends sensor data (distance and image) to the laptop and executes the commands received.
- **`robot/camera.py`**: Captures images using the Raspberry Pi Camera.
- **`robot/ultrasonic.py`**: Reads distance data from the ultrasonic sensor.

### **Shared**
- **`shared/config.py`**: Configuration file containing settings like the laptop's IP address.

---

## **Usage**

### **On the Laptop:**
1. Ensure Flask is running:
   ```bash
   python laptop/app.py
   ```
2. The Flask server will listen on your laptop's IP (`http://192.168.137.235:5000`).

### **On the Raspberry Pi:**
1. Ensure the Raspberry Pi is connected to the same network as the laptop.
2. Run the robot control program:
   ```bash
   python robot/main.py
   ```

The robot will start sending sensor data to the laptop, which will respond with movement commands. The robot will then execute these commands.

---

## **Additional Notes**
- Ensure that the Raspberry Pi and the laptop are on the same local network.
- Modify the `move_robot` function in `robot/main.py` to include the actual motor control logic for your robot.
- You can expand this project by integrating object detection, more sensors, or adding more complex logic to the Flask API and Deepseek processing.
