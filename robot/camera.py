from picamera2 import Picamera2

picam2 = Picamera2()

# Initialize camera and start capture
picam2.start()

def capture_image():
    picam2.capture_file("latest_image.jpg")
    print("Image captured!")
