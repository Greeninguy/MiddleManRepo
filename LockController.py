def setup():
    import RPi.GPIO as GPIO
    

    GPIO.setmode(GPIO.Board)
    GIOP.setwarnings(False)

    ledPin = 11

    GPIO.setup(ledPin, GPIO.OUT)

def lock():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.Board)
    GIOP.setwarnings(False)
    ledPin = 11
    GPIO.setup(ledPin, GPIO.OUT)
    import time
    import datetime
    from datetime import datetime
    
    print("Locking Gate.")
    d = datetime.today()
    t = d.timetuple()
    f = open("lockday.txt", 'a')
    f.write(str(d.weekday()))
    f.write('\n')
    f.close()
    f = open("lockhour.txt", 'a')
    f.write(str(t[3]))
    f.write('\n')
    f.close()
    f = open("lockminute.txt", 'a')
    f.write(str(t[4]))
    f.write('\n')
    f.close()
    GPIO.output(ledPin, GPIO.HIGH)

def unlock():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.Board)
    GIOP.setwarnings(False)
    ledPin = 11
    GPIO.setup(ledPin, GPIO.OUT)
    import time
    import datetime
    from datetime import datetime
    
    print("Unlocking Gate.")
    d = datetime.today()
    t = d.timetuple()
    f = open("unlockday.txt", 'a')
    f.write(str(d.weekday()))
    f.write('\n')
    f.close()
    f = open("unlockhour.txt", 'a')
    f.write(str(t[3]))
    f.write('\n')
    f.close()
    f = open("unlockminute.txt", 'a')
    f.write(str(t[4]))
    f.write('\n')
    f.close()
    GPIO.output(ledPin, GPIO.LOW)

def lockAfterUnlock():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.Board)
    GIOP.setwarnings(False)
    ledPin = 11
    GPIO.setup(ledPin, GPIO.OUT)
    
    print("Unlocking Gate.")
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(5)
    GPIO.output(ledPin, GPIO.HIGH)

def lockMenu():
    while True:
        print("Which Operation? \n"
              "Lock: L \n"
              "Unlock: U \n"
              "Unlock and Relock: P \n"
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
