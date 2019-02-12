import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
my_pwm=GPIO.PWM(17,100)
my_pwm.start(0)
bright=50

try: 
        while True:
                        my_pwm.ChangeDutyCycle(2*bright)
                        time.sleep(0.05)
                        my_pwm.ChangeDutyCycle(0)
                        time.sleep(0.05)
except KeyBoardInterrupt:
        pass

my_pwm.stop()
GPIO.cleanup()

