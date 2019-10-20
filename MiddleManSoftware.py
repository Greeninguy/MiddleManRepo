
while True:
    print("Which Feature? \n"
          "Led Light: L \n"
          "Magnetic Lock: M \n"
          "Height Sensor: H \n"
          "Exit: E \n")
    answer = input()
    if answer == "l" or answer == "L":
        import LEDController
    elif answer == "m" or answer == "M":
        import LockController
    elif answer == "h" or answer == "H:":
        import sensorController
    elif answer == "e" or answer == "E":
        GPIO.cleanup()
        print("Exiting program...")
        exit()
    else:
        print("Invalid input")
