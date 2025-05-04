Server Info
A simple Python script to display and log system information.
Description
Server Info is a lightweight Python utility that provides essential information about your system, including:

OS details and version
CPU usage and core count
Memory and disk usage
System uptime
Network information
Running processes
Hardware model information

The script logs this information to a file for record-keeping and system monitoring purposes.
Requirements

Python 3.6+
psutil library

Installation

Clone this repository:
git clone https://github.com/gagan-lb/server_info.git
cd server_info

Install the required dependencies:
pip install psutil


Usage
Run the script with Python:
python server_info.py
The script will display system information in the console and save it to a log file named server_info.log in the same directory.
