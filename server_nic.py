#!/usr/bin/env python3
"""
Server NIC Information Script
Displays network card model, speed, and driver information.
"""

import os
import subprocess

def get_nic_info():
    print("=== SERVER NIC INFORMATION ===")
    
    # Get interfaces (excluding loopback)
    interfaces = [iface for iface in os.listdir('/sys/class/net/') if iface != 'lo']
    
    for iface in sorted(interfaces):
        print(f"\nInterface: {iface}")
        
        # Get MAC address
        try:
            with open(f'/sys/class/net/{iface}/address', 'r') as f:
                print(f"MAC: {f.read().strip()}")
        except:
            pass
        
        # Get link speed
        try:
            with open(f'/sys/class/net/{iface}/speed', 'r') as f:
                speed = f.read().strip()
                if speed.isdigit():
                    print(f"Speed: {speed} Mbps")
        except:
            pass
        
        # Get driver name
        try:
            if os.path.exists(f'/sys/class/net/{iface}/device/driver'):
                driver_path = os.readlink(f'/sys/class/net/{iface}/device/driver')
                print(f"Driver: {os.path.basename(driver_path)}")
        except:
            pass
        
        # Get model info (from lspci for physical devices)
        try:
            if os.path.exists(f'/sys/class/net/{iface}/device/vendor') and \
               os.path.exists(f'/sys/class/net/{iface}/device/device'):
                with open(f'/sys/class/net/{iface}/device/vendor', 'r') as f:
                    vendor = f.read().strip()
                with open(f'/sys/class/net/{iface}/device/device', 'r') as f:
                    device = f.read().strip()
                
                # Use lspci for device name
                cmd = f"lspci -mm -d {vendor.replace('0x', '')}:{device.replace('0x', '')}"
                output = subprocess.getoutput(cmd)
                if output:
                    parts = output.split('"')
                    if len(parts) >= 4:
                        print(f"Model: {parts[3]}")
        except:
            pass
        
        # Get firmware version (if ethtool is available)
        try:
            firmware = subprocess.getoutput(f"ethtool -i {iface} 2>/dev/null | grep 'firmware-version:' | cut -d ' ' -f 2")
            if firmware:
                print(f"Firmware: {firmware}")
        except:
            pass

if __name__ == "__main__":
    get_nic_info()
