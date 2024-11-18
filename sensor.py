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


def detect_motion_webcam():
    global previous_frame
    ret, current_frame = cap.read()
    if not ret:
        return False

    motion_detected = False
    if previous_frame is not None:
        gray_current = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
        gray_previous = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(gray_previous, gray_current)
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

        motion_detected = cv2.countNonZero(thresh) > 5000

    if motion_detected:
        capture_image("gpio_motion")

    previous_frame = current_frame
    return motion_detected


async def get_sensor_data():
    try:
        dht_data = read_dht22_data()
        gpio_data = read_gpio_data()
        motion_webcam = detect_motion_webcam()

        return {
            **dht_data,
            **gpio_data,
            "motion_detected": motion_webcam
        }
    except Exception as error:
        sensor.exit()
        cap.release()
        raise error


def get_cpu_temperature():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = int(f.read()) / 1000.0
            return temp
    except FileNotFoundError:
        return None