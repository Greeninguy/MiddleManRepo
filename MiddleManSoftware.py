import automation
import datetime
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LEDOnDay[]
LEDOnHour[]
LEDOnMinute[]

LEDOffDay[]
LEDOffHour[]
LEDOffMinute[]

lockDay[]
lockHour[]
lockMinute[]

unlockDay[]
unlockHour[]
unlockMinute[]

def LEDOnDayAdd(i):
    LEDDay.append(i)

def LEDOnHourAdd(i):
    LEDHour.append(i)

def LEDOnMinuteAdd(i):
    LEDMinute.append(i)

def LEDOffDayAdd(i):
    LEDDay.append(i)

def LEDOffHourAdd(i):
    LEDHour.append(i)

def LEDOffMinuteAdd(i):
    LEDMinute.append(i)

def LockDayAdd(i):
    lockDay.append(i)

def LockHourAdd(i):
    lockHour.append(i)

def LockinuteAdd(i):
    lockMinute.append(i)

def UnlockDayAdd(i):
    unlockDay.append(i)

def UnlockHourAdd(i):
    unlockHour.append(i)

def UnlockinuteAdd(i):
    unlockMinute.append(i)

while True:
    print("Which Feature? \n"
          "Led Light: L \n"
          "Magnetic Lock: M \n"
          "Height Sensor: H \n"
          "Exit: E \n")
    answer = input()
    if answer == "l" or answer == "L":
        import LEDController
        LEDController.LEDMenu()
    elif answer == "m" or answer == "M":
        import LockController
        LockController.lockMenu()
    elif answer == "h" or answer == "H:":
        import sensorController
        sensorController.sensorMenu()
    elif answer == "e" or answer == "E":
        GPIO.cleanup()
        print("Exiting program...")
        exit()
    else:
        print("Invalid input")
