This is a python script to log gps data on android phone using termux.

Requirements:

python

Termux

Termux-API

Termux-Sensors

Installation:
1. Put python file in home directory
2. Install termux and dependencies
3. Change accelerometer sensor name to one on your phone
4. Setup cron to run script at whatever interval you want
5. Modify logger to save in format you need
6. Give termux wakelock

Optional:
-Termux-Boot: Have cron and wakelock run when phone is powered on.

The python script reads accelerometer twice and compares the data, if phone is sitting still on a table, etc, the gps will not be read. Otherwise, gps will be read and logged to csv file.
