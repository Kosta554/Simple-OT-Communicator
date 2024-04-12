# Simple-OT-Communicator

Simple-OT-Communicator is a basic client-server communication application built in Python using sockets. It allows for the transmission of messages between a client and a server over a network connection.

![Simple to communicator GitHub pic drawio 2](https://github.com/Kosta554/Simple-OT-Communicator/assets/24320290/a58db57d-713f-4928-816b-504b8afbcff3)

## Features

- **Client-Server Architecture:** Utilizes a client-server model for communication.
- **Basic Messaging:** Allows clients to send messages to the server, which are then displayed.
- **Emergency Stop:** Includes a feature for triggering an emergency stop by pressing a button on the Raspberry Pi client.

## Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/Simple-OT-Communicator.git
    ```

2. **Run the Server:**
    ```bash
    python server.py
    ```

3. **Run the Client:**
    ```bash
    python client.py
    ```

4. **Press Emergency Stop:**
    - If using the Raspberry Pi client, press the emergency stop button to send an emergency stop message to the server.

## Requirements

- Python 3.x
- Raspberry Pi (for using the emergency stop feature)
- RPi.GPIO library (for Raspberry Pi GPIO interaction)

## Configuration

- **Port Number:** By default, the server listens on port 52784. You can modify this in the `Server.py` file.
- **Emergency Button Pin:** In the `Client.py` file, you can configure the GPIO pin used for the emergency stop button on the Raspberry Pi.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
