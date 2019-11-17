import LEDController
import LockController
import os
import datetime
from datetime import datetime

automate()

def automate():
    try:
        while True:
            time = timeCheck()
            match = readAuto("LEDOnAuto.txt")
            if match:
                LEDController.turnOn()
            match = readAuto("LEDOffAuto.txt")
            if match:
                LEDController.turnOff()
            match = readAuto("LockAuto.txt")
            if match:
                LockController.lock()
            match = readAuto("UnlockAuto.txt")
            if match:
                LockController.unlock()
            time.sleep(60)
    except KeyboardInterrupt:
        exit()

def readAuto(file, time):
    if os.stat(file).st_size == 0:
        return false
    f = open(file, 'r')
    lis = f.read().splitlines()
    f.close()
    lis = list(map(int,lis))
    if file[0] == time[0] and file[1] == time[1] and file[2] == time[2]:
        return true
    else:
        return false

def timeCheck():
    d = datetime.today()
    t = d.timetuple()
    time = []
    time.append(d.weekday())
    time.append(t[3])
    time.append(t[4])
    return time
