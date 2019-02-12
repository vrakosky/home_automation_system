import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT)

p = GPIO.PWM(4,50)
p.start(1)

# try:
#         while True:
for i in range(100):
                        p.ChangeDutyCycle(i)
                        time.sleep(0.02)
for i in range(100):
                        p.ChangeDutyCycle(100-1)
                        time.sleep(0.02)
# except KeyBoardInterrupt:
#         pass

p.stop()
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4,1)


