import socket

HOST = 'localhost'  # Change this to your server's IP address or '0.0.0.0' for all interfaces
PORT = 52784         # Change this to the port you want to listen on
STATUS_SERVER_HOST = 'status_server_ip'  # Change this to the IP address of the status server
STATUS_SERVER_PORT = 12345  # Change this to the port the status server is listening on

def send_status_update(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((STATUS_SERVER_HOST, STATUS_SERVER_PORT))
        s.sendall(message.encode())
        print(f"Sent status update '{message}' to status server.")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    try:
                        data = conn.recv(1024)
                        if not data:
                            break
                        message = data.decode()
                        print(f"Received: {message}")
                        if message == "Emergency Stop":
                            print("Emergency stop activated.")
                            send_status_update("Device Not Operational")
                    except KeyboardInterrupt:
                        print("Emergency stop activated.")
                        break

if __name__ == "__main__":
    main()
    
