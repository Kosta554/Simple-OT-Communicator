import socket
import time
import RPi.GPIO as GPIO

HOST = 'IP'  # Change this to the IP address of your server if not running locally
PORT = 52784        # Change this to the port your server is listening on
EMERGENCY_PIN = 17   # Change this to the GPIO pin you're using for the emergency button

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(EMERGENCY_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            messages = ["Scanning", "Sorting", "Done"]
            for message in messages:
                s.sendall(message.encode())
                print(f"Sent: {message}")
                time.sleep(4)

                if GPIO.input(EMERGENCY_PIN) == GPIO.LOW:
                    print("Emergency stop button pressed!")
                    s.sendall("Emergency Stop".encode())
                    break

if __name__ == "__main__":
    main()
