import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ledPin = 31

GPIO.setup(ledPin, GPIO.OUT)

def turnOn():
    print("Turning on light.")
    GPIO.output(ledPin, GPIO.HIGH)

def turnOff():
    print("Turning off light.")
    GPIO.output(ledPin, GPIO.LOW)

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
        GPIO.cleanup()
        print("Exiting program...")
        exit()
    else:
        print("Invalid input")
