#!/usr/bin/env python3

import socket
import platform
import os

print("===== Basic System Info =====")
print("Hostname:", socket.gethostname())
print("IP Address:", socket.gethostbyname(socket.gethostname()))
print("OS:", platform.system(), platform.version())
print("Kernel:", platform.release())
print("CPU:", platform.processor())
print("CPU Cores:", os.cpu_count())

print("\n===== Hardware & Memory =====")
os.system("echo -n 'Memory: '; grep MemTotal /proc/meminfo")
os.system("echo -n 'Hardware: '; cat /sys/class/dmi/id/sys_vendor 2>/dev/null; cat /sys/class/dmi/id/product_name 2>/dev/null")

print("\n===== NIC Info =====")
# Loop through the network interfaces and get MAC addresses, ignore errors for special files
os.system("for iface in $(ls /sys/class/net/); do "
          "if [ -e /sys/class/net/$iface/address ]; then "
          "echo \"$iface $(cat /sys/class/net/$iface/address)\"; "
          "fi; done")

print("\n===== System Status =====")
os.system("echo -n 'Uptime: '; uptime -p")
os.system("echo 'Disk Usage:'; df -h --total | grep total")
os.system("echo -n 'Load Average: '; cat /proc/loadavg")
os.system("echo -n 'Running Processes: '; ps -e --no-headers | wc -l")

