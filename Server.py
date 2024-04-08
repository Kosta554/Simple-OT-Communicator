import socket

HOST = 'localhost'  # Change this to your server's IP address or '0.0.0.0' for all interfaces
PORT = 12345         # Change this to the port you want to listen on

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode()}")

if __name__ == "__main__":
    main()
