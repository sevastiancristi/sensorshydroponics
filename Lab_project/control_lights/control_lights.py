import RPi.GPIO as GPIO
from sys import argv
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
if "on" in argv[1]:
    GPIO.output(26, GPIO.LOW)
    print("Leds on!")
elif "off" in argv[1]:
    GPIO.cleanup(26)
    print("Leds off!")
else:
    print("I can't understand...")
