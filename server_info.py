k#!/usr/bin/env python3
"""
System Information Script
A simple script to display system information like OS, CPU, memory, and disk usage.
"""

import platform
import psutil
import datetime
import socket
import logging

def get_system_info():
    # Get all system information at once with uname()
    system_info = platform.uname()

    print("=" * 50)
    print("SYSTEM INFORMATION REPORT")
    print("=" * 50)

    # Display uname information
    print(f"OS: {system_info.system} {system_info.release}")
    print(f"Hostname: {system_info.node}")
    print(f"Version: {system_info.version}")
    print(f"Machine Architecture: {system_info.machine}")
    print(f"Processor: {system_info.processor}")

    # Get CPU information using psutil
    print(f"CPU Cores: {psutil.cpu_count(logical=False)}")
    print(f"CPU Usage: {psutil.cpu_percent()}%")

    # Get memory information
    mem = psutil.virtual_memory()
    print(f"Memory: {mem.used/1073741824:.1f}GB / {mem.total/1073741824:.1f}GB ({mem.percent}%)")

    # Get disk information
    disk = psutil.disk_usage('/')
    print(f"Disk: {disk.used/1073741824:.1f}GB / {disk.total/1073741824:.1f}GB ({disk.percent}%)")

    # Calculate system uptime
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time
    print(f"Uptime: {uptime}")
    
    # Check network information
    print("\nNetwork Information:")
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"IP Address: {ip_address}")
    net_io = psutil.net_io_counters()
    print(f"Bytes Sent: {net_io.bytes_sent/1048576:.2f} MB")
    print(f"Bytes Received: {net_io.bytes_recv/1048576:.2f} MB")
    
    # Display running processes
    print("\nRunning Processes:")
    for i, proc in enumerate(psutil.process_iter(['pid', 'name'])):
        print(f"{proc.info['pid']} - {proc.info['name']}")
        if i >= 4:  # Show just top 5 processes (0-4)
            break
    
    # HW models
    print("\nHardware Model:")
    print(f"System: {platform.machine()}")
    
    # Log information to a file
    logging.basicConfig(filename='server_info.log', level=logging.INFO)
    logging.info(f"System Report: {datetime.datetime.now()}")
    logging.info(f"OS: {system_info.system} {system_info.release}")
    logging.info(f"Memory: {mem.percent}%")
    logging.info(f"Disk: {disk.percent}%")

    print("=" * 50)

if __name__ == "__main__":
    get_system_info()
