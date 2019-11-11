import LEDController
import LockController
import sensorController
import AutomationData
import datetime
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

while True:
    print("Which Feature? \n"
          "Led Light: L \n"
          "Magnetic Lock: M \n"
          "Height Sensor: H \n"
          "Automation/Data A \n"
          "Exit: E \n")
    answer = input()
    if answer == "l" or answer == "L":
        LEDController.LEDMenu()
    elif answer == "m" or answer == "M":   
        LockController.lockMenu()
    elif answer == "h" or answer == "H:":        
        sensorController.sensorMenu()
    elif answer == 'a' or answer == 'A':       
        AutomationData.autoMenu()
    elif answer == "e" or answer == "E":
        GPIO.cleanup()
        print("Exiting program...")
        exit()
    else:
        print("Invalid input")
