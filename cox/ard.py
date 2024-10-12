import serial
import time

# Initialize serial connections for both Arduinos
arduino1 = serial.Serial('COM5', 9600, timeout=1)
arduino2 = serial.Serial('COM6', 9600, timeout=1)

# Allow time for connections to establish
time.sleep(2)

def read_speed(serial_connection):
    try:
        data = serial_connection.readline().decode().strip()
        return float(data)
    except (ValueError, serial.SerialException):
        return None

while True:
    # Read speed data from both Arduinos
    speed1 = read_speed(arduino1)
    speed2 = read_speed(arduino2)

    # Ensure both speeds are valid before comparison
    if speed1 is not None and speed2 is not None:
        if speed1 > speed2:
            print(f"Arduino 1 is faster by {speed1 - speed2:.2f}")
        elif speed2 > speed1:
            print(f"Arduino 2 is faster by {speed2 - speed1:.2f}")
        else:
            print("Both Arduinos have the same speed.")

    # Wait a bit before reading the next set of values
    time.sleep(0.5)
