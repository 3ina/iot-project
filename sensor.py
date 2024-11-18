import board
from gpiozero import Button
import adafruit_dht
import cv2
import time

sensor = adafruit_dht.DHT22(board.D4)
mq9_sensor = Button(17)

cap = cv2.VideoCapture(0)
previous_frame = None

IMAGE_SAVE_DIR = "captured_images"

def read_dht22_data():
    try:
        temperature_c = sensor.temperature
        temperature_f = temperature_c * (9 / 5) + 32 if temperature_c is not None else None
        humidity = sensor.humidity
        return {"temperature_c": temperature_c, "temperature_f": temperature_f, "humidity": humidity}
    except RuntimeError as error:
        print(f"Error reading DHT22 sensor data: {error}")
        return {}


def read_gpio_data():
    gas_detected = mq9_sensor.is_pressed

    return {
        "gas_detected": gas_detected
    }

def capture_image(source):
    timestamp = int(time.time())
    filename = f"{IMAGE_SAVE_DIR}/{source}_motion_{timestamp}.jpg"
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)
        print(f"Image saved: {filename}")
    else:
        print("Failed to capture image.")