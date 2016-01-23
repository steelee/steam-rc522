import time
import subprocess
import serial

games = {'DOTA' : r'D:\Games\SteamInstall\steamapps\common\dota 2 beta\game\bin\win64\dota2.exe',
		 'ROCKET' : r'D:\Games\SteamInstall\steamapps\common\rocketleague\Binaries\Win32\RocketLeague.exe' }

ser = serial.Serial('COM4', 9600)

print("Prepare to recieve")
time.sleep(1)

while True:
	message = ser.readline()
	message = str(message)
	message = message[3:50].replace(" ","")
	message = ''.join(chr(int(message[i:i+2],16)) for i in range(0,len(message),2)).rstrip(' \t\r\n\0')
	if message in games:
		break
	time.sleep(1)
subprocess.call(['start.bat',games[message]])