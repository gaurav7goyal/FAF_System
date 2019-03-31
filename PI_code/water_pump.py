import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

# Declare the GPIO settings
GPIO.setmode(GPIO.BCM)
def mot(a):
    GPIO.setup(a, GPIO.OUT)
    GPIO.output(a, GPIO.HIGH) # Set AIN1
    print("yes")
    time.sleep(2)
    GPIO.output(a, GPIO.LOW) # Set AIN2

