import socket
import time

HOST = 'localhost'  # Change this to the IP address of your server if not running locally
PORT = 12345         # Change this to the port your server is listening on

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            messages = ["Scanning", "Sorting", "Done"]
            for message in messages:
                s.sendall(message.encode())
                print(f"Sent: {message}")
                time.sleep(4)

if __name__ == "__main__":
    main()
