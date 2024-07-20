import subprocess
import json
import time

def check_move():
	read1=subprocess.getstatusoutput('termux-sensor -s Accel -n 1')
	read2=subprocess.getstatusoutput('termux-sensor -s Accel -n 1')
	r1=json.loads(read1[1])
	r2=json.loads(read2[1])
  #replace sensor name with accelerometer sensor name from your device
	data1=r1["mc34x9 Accelerometer Non-wakeup"]["values"]
	data2=r2["mc34x9 Accelerometer Non-wakeup"]["values"]
	count=0
	moving=False
	for items in data1:
		if data1[count]!=data2[count]:
			moving=True
	if moving==True:
		return True

if check_move()==True:
	data=subprocess.getstatusoutput('termux-location')
	d=json.loads(data[1])
	
	with open("loc.csv", "a") as locLog:
		locLog.write(f"{round(time.time())},{d['latitude']},{d['longitude']},{round(d['speed'])},{round(d['bearing'])},{round(d['altitude'])}\n")
