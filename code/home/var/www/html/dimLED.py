#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

p = GPIO.PWM(17,100)

p.start(0)

try: 
        while True:
                        p.ChangeDutyCycle(100)
                        time.sleep(0.02)
except KeyBoardInterrupt:
        pass

p.stop()

GPIO.cleanup()
