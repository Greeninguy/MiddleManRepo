def setup():   
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    ledPin = 31

    GPIO.setup(ledPin, GPIO.OUT)

def turnOn():
    setup()
    print("Turning on light.")
    d = datetime.today()
    t = d.timetuple()
    MiddleManSoftware.LEDOnDayAdd(t[2])
    MiddleManSoftware.LEDOnHourAdd(t[3])
    MiddleManSoftware.LEDOnMinuteAdd(t[4])
    GPIO.output(ledPin, GPIO.HIGH)

def turnOff():
    setup()
    print("Turning off light.")
    d = datetime.today()
    t = d.timetuple()
    MiddleManSoftware.LEDOffDayAdd(t[2])
    MiddleManSoftware.LEDOffHourAdd(t[3])
    MiddleManSoftware.LEDOffMinuteAdd(t[4])
    GPIO.output(ledPin, GPIO.LOW)
    
def LEDMenu():
    while True:
        print("Which Operation? \n"
            "Turn On: T \n"
            "Turn Off: R \n"
            "Exit: E \n")
        answer = input()
        if answer == "t" or answer == "T":
            turnOn()
        elif answer == "r" or answer == "R":
            turnOff()
        elif answer == "e" or answer == "E":
            print("Exiting program...")
            exit()
        else:
            print("Invalid input")
