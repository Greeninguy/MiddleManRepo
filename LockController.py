import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.Board)
GIOP.setwarnings(False)

ledPin = 11

GPIO.setup(ledPin, GPIO.OUT)

def lock():
    print("Locking Gate.")
    GPIO.output(ledPin, GPIO.HIGH)

def unlock():
    print("Unlocking Gate.")
    GPIO.output(ledPin, GPIO.LOW)

def lockAfterUnlock():
    print("Unlocking Gate.")
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(5)
    GPIO.output(ledPin, GPIO.HIGH)

def lockMenu:
    while True:
        print("Which Operation? \n"
              "Lock: L \n"
              "Unlock: U \n"
              "Unlock and Relock: P
              "Exit: E \n")
        answer = input()
        if answer == "l" or answer == "L":
            lock()
        elif answer == "u" or answer == "U":
            unlock()
        elif answer == "p" or answer == "P":
            lockAfterUnlock()
        elif answer == "e" or answer == "E":
            print("Exiting program...")
            exit()
        else:
            print("Invalid input")
