# Server Info Script

This Python script is designed to gather basic system information on a Linux server. It provides useful details about the system such as:

- Hostname
- IP address
- Operating System and Kernel
- CPU information
- Memory
- Network Interface Cards (NICs) and their MAC addresses
- System uptime, disk usage, load average, and running processes

## Features
- Displays hostname and IP address
- Shows system OS, kernel version, and CPU details
- Prints memory information and system hardware model
- Lists all NICs along with their MAC addresses
- Provides system uptime, disk usage, load average, and process count

## Requirements
- Python 3.x
- Basic Linux commands (e.g., `ls`, `cat`, `df`, `uptime`)

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/gagan-lb/server_info.git
    ```

2. Change to the script directory:
    ```bash
    cd server_info
    ```

3. Make the script executable:
    ```bash
    chmod +x serverspecs.py
    ```

4. Run the script:
    ```bash
    ./serverspecs.py
    ```

   Or run it using Python:
    ```bash
    python3 serverspecs.py
    ```



