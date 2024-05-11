import socket
import sys
import configparser
from cryptography.fernet import Fernet

# Load configuration from a file or command line arguments
config = configparser.ConfigParser()
config.read('client.ini')
HOST = config['DEFAULT'].get('Host', 'localhost')
PORT = config['DEFAULT'].getint('Port', 52784)

# Encryption setup
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def send_command_and_messages(command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            encrypted_command = cipher_suite.encrypt(command.encode())
            s.sendall(encrypted_command)
            print(f"Sent encrypted command: {command}")
            handle_command_responses(s)
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def handle_command_responses(sock):
    if command == "start":
        try:
            messages = ["Scanning", "Sorting", "Done"]
            for message in messages:
                encrypted_message = cipher_suite.encrypt(message.encode())
                sock.sendall(encrypted_message)
                print(f"Sent encrypted message: {message}")
                time.sleep(1)
        except KeyboardInterrupt:
            encrypted_stop = cipher_suite.encrypt("Emergency Stop".encode())
            sock.sendall(encrypted_stop)
            print("Emergency stop activated.")
    elif command == "stop":
        encrypted_stop = cipher_suite.encrypt("Stop".encode())
        sock.sendall(encrypted_stop)
        print("Sent encrypted stop command.")
    elif command == "restart":
        encrypted_restart = cipher_suite.encrypt("Restart".encode())
        sock.sendall(encrypted_restart)
        print("Sent encrypted restart command.")

def main():
    while True:
        command = input("Enter command (Start, Stop, Restart): ").strip().lower()
        if command in ["start", "stop", "restart"]:
            send_command_and_messages(command)
        else:
            print("Invalid command. Please enter 'Start', 'Stop', or 'Restart'.")

if __name__ == "__main__":
    main()
 
