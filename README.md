# Server Information Script

A simple Python script that displays comprehensive system information including OS details, CPU usage, memory utilization, disk space, and system uptime.

## Features

- Shows operating system details (name, version, architecture)
- Displays CPU information (cores and current usage)
- Shows memory usage (used/total and percentage)
- Shows disk usage (used/total and percentage)
- Displays system uptime since last boot

## Requirements

This script requires the following Python libraries:

- platform (standard library)
- psutil (needs to be installed)
- datetime (standard library)

## Installation

Make sure you have Python 3 installed on your system. Install the required psutil library:

```bash
pip install psutil
```

## Usage

Simply run the script:

```bash
python system_info.py
```

## Sample Output

```
SYSTEM INFORMATION REPORT
=========================

OS: Linux 5.14.0-362.8.1.el9_3.x86_64 Hostname: target2 Version: #1 SMP PREEMPT_DYNAMIC Wed Nov 8 17:36:32 UTC 2023
Machine Architecture: x86_64 Processor: x86_64
CPU Cores: 64 CPU Usage: 85.7%
Memory: 172.66GB / 251.0GB (69.4%)
Disk: 9.0GB / 69.9GB (12.9%)
Uptime: 33 days, 2:37:57.823125

Network Information: IP Address: 192.168.40.49
Bytes Sent: 1993808.96 MB
Bytes Received: 2402063.17 MB

Running Processes: 1 - systemd 2 - kthreadd 3 - rcu_gp 4 - rcu_par_gp 5 - slub_flushwq

Hardware Model: System: x86_64
