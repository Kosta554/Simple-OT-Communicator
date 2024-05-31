# Simple OT Communicator

## Introduction
Simple OT Communicator is a client-server application designed for operational technology (OT) environments, leveraging Python sockets for communication. It supports secure and reliable messaging capabilities across networked devices.

![Simple OT Communicator Diagram](https://github.com/Kosta554/Simple-OT-Communicator/assets/24320290/a58db57d-713f-4928-816b-504b8afbcff3)

## Features
- **Client-Server Architecture**: Enables robust communication using a client-server model.
- **Enhanced Security**: Incorporates encryption to secure messages transmitted over the network.
- **Configurable Settings**: Customize settings such as IP address and port via `client.ini`.
- **Emergency Stop**: Supports an emergency stop feature, which can now be triggered with enhanced security.

## Usage
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Kosta554/Simple-OT-Communicator.git
    ```
2. **Configure the Application**:
    - Edit `client.ini` for client settings.
    - Ensure matching encryption keys on both client and server.
3. **Run the Server**:
    ```bash
    python Server.py
    ```
4. **Run the Client**:
    ```bash
    python Client.py
    ```
   Follow the prompts to send secure commands.

## Requirements
- Python 3.x
- Cryptography package (install with `pip install cryptography`)

## Configuration
- **Host and Port**: Set in `client.ini` or directly in the script files.
- **Encryption**: Ensure the client and server scripts are configured with the same encryption key.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any bugs or feature suggestions.

## License
This project is licensed under the [GNU General Public License v3.0](LICENSE).
