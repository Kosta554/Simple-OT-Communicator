import socket
import logging

# Setup logging
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

HOST = 'localhost'  # Server's IP address or '0.0.0.0' for all interfaces
PORT = 52784        # Port to listen on
MONITORING_HOST = 'monitoring_server_ip'  # IP of the monitoring server
MONITORING_PORT = 12345                   # Port the monitoring server listens on

def send_error_code(error_code, description):
    """ Sends error codes to a monitoring server for NIDS to pick up. """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:  # Using UDP
        message = f"{error_code}: {description}"
        sock.sendto(message.encode(), (MONITORING_HOST, MONITORING_PORT))
        logging.info(f"Error code sent: {message}")

def main():
    server_running = True
    while server_running:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.bind((HOST, PORT))
                    s.listen()
                    logging.info("Server listening on {}:{}".format(HOST, PORT))
                except socket.error as e:
                    send_error_code(2, "Cannot bind to {}:{}. Details: {}".format(HOST, PORT, e))
                    break  # Exit the server loop if binding fails

                while True:
                    conn, addr = s.accept()
                    with conn:
                        logging.info("Connected by {}".format(addr))
                        while True:
                            data = conn.recv(1024)
                            if not data:
                                send_error_code(4, "Lost connection with host.")
                                break
                            message = data.decode()
                            process_message(message)
        except KeyboardInterrupt:
            send_error_code(3, "Server shutdown requested via KeyboardInterrupt.")
            server_running = False
        except Exception as e:
            send_error_code(3, "Unexpected server error. Details: {}".format(e))
            server_running = False  # Optionally restart or shut down depending on policy

def process_message(message):
    if message == "Emergency Stop":
        send_error_code(1, "Emergency stop activated.")
    else:
        logging.info("Received: {}".format(message))

if __name__ == "__main__":
    main()
