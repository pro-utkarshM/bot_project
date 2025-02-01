import requests
from camera import capture_image
from ultrasonic import get_distance
from shared.config import laptop_ip
import time

# Function to move robot based on command
def move_robot(command):
    if "move forward" in command:
        print("Moving forward...")
        # Call motor control here
    elif "turn left" in command:
        print("Turning left...")
        # Call motor control here
    elif "stop" in command:
        print("Stopping...")
        # Call motor control here

# Main loop to send sensor data and execute commands
while True:
    # Get distance from ultrasonic sensor
    distance = get_distance()

    # Capture image from camera
    capture_image()

    # Send data to laptop and get command
    data = {
        "distance": distance
    }
    files = {"image": open("latest_image.jpg", "rb")}
    response = requests.post(f"http://{laptop_ip}:5000/data", json=data, files=files)
    command = response.json()["command"]
    
    # Move the robot based on the command
    move_robot(command)

    # Delay for next cycle (adjust as needed)
    time.sleep(1)
