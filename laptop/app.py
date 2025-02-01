from flask import Flask, request, jsonify
import subprocess
from deepseek_query import get_deepseek_command

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def process_data():
    # Retrieve sensor and camera data from Pi
    distance = request.json["distance"]
    image = request.files["image"]

    # Save the image
    image.save("latest_image.jpg")

    # Process command using deepseek model based on sensor data
    command = get_deepseek_command(distance)
    
    # Respond with the command
    return jsonify({"command": command})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
