# System Information Script

A simple Python script that displays comprehensive system information including OS details, CPU usage, memory utilization, disk space, and system uptime.

## Features

- Shows operating system details (name, version, architecture)
- Displays CPU information (cores and current usage)
- Shows memory usage (used/total and percentage)
- Shows disk usage (used/total and percentage)
- Displays system uptime since last boot

## Requirements

This script requires the following Python libraries:
- `platform` (standard library)
- `psutil` (needs to be installed)
- `datetime` (standard library)

## Installation

1. Make sure you have Python 3 installed on your system
2. Install the required `psutil` library:

```
pip install psutil
```

## Usage

Simply run the script:

```
python system_info.py
```

