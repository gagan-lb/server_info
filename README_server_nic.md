	# Server NIC Information Script

A lightweight Python script that displays network interface information on server systems.

## Overview

This script provides essential information about your server's network interfaces:
- MAC address
- Link speed
- Driver name
- Hardware model
- Firmware version

## Requirements

- Server running Linux operating system
- Python 3
- Standard utilities:
  - ethtool (optional, for firmware information)
  - lspci (optional, for model information)

## Usage

1. Save the script as `server_nic.py`
2. Make it executable:
   ```
   chmod +x server_nic.py
   ```
3. Run the script:
   ```
   ./server_nic.py
   ```

For complete information, you may need to run with sudo:
```
sudo ./server_nic.py
```

## Sample Output

```
=== SERVER NIC INFORMATION ===

Interface: eno1
MAC: 00:1f:c6:9d:42:31
Speed: 1000 Mbps
Driver: e1000e
Model: Intel Corporation Ethernet Connection I219-LM
Firmware: 0.5-4

Interface: eno2
MAC: 80:32:53:d4:a2:b7
Speed: 10000 Mbps
Driver: ixgbe
Model: Intel Corporation 82599ES 10-Gigabit SFI/SFP+ Network Connection
Firmware: 3.16-1
```

## How It Works

The script reads information from system files and uses basic commands:
- Reads from `/sys/class/net/` directory
- Uses `lspci` to get hardware model information
- Uses `ethtool` to retrieve firmware version

## License

This script is released under the MIT License. Feel free to use and modify it as needed.
