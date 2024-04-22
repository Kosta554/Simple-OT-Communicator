import socket
import time
import sys

HOST = 'localhost'  # Change this to the IP address of your server if not running locally
PORT = 52784         # Change this to the port your server is listening on

def send_command_and_messages(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(command.encode())
        print(f"Sent command: {command}")
        if command == "start":
            try:
                while True:
                    messages = ["Scanning", "Sorting", "Done"]
                    for message in messages:
                        s.sendall(message.encode())
                        print(f"Sent message: {message}")
                        time.sleep(1)
            except KeyboardInterrupt:
                s.sendall("Emergency Stop".encode())
                print("Emergency stop activated.")
                return
        elif command == "stop":
            s.sendall("Stop".encode())
            print("Sent stop command.")
        elif command == "restart":
            s.sendall("Restart".encode())
            print("Sent restart command.")

def main():
    while True:
        command = input("Enter command (Start, Stop, Restart): ").strip().lower()
        if command in ["start", "stop", "restart"]:
            send_command_and_messages(command)
        else:
            print("Invalid command. Please enter 'Start', 'Stop', or 'Restart'.")

if __name__ == "__main__":
    main()
