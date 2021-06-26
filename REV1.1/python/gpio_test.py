import RPi.GPIO as GPIO
from time import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.output(16, GPIO.LOW)
GPIO.output(26, GPIO.LOW)
GPIO.output(22, GPIO.LOW)

GPIO.output(16, GPIO.HIGH)
sleep(1)
GPIO.output(16, GPIO.LOW)
GPIO.output(26, GPIO.HIGH)
sleep(1)
GPIO.output(26, GPIO.LOW)


for x in range(30000):
	GPIO.output(22, GPIO.HIGH)
	sleep(0.00017)
	GPIO.output(22, GPIO.LOW)
	sleep(0.00017)

GPIO.output(22, GPIO.LOW)