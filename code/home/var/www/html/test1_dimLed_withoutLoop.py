import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

p = GPIO.PWM(17, 50)
p.start(1)
p.ChangeFrequency(22)
 #raw_input('Press return to stop:')   # use raw_input for Python 2
p.stop()
GPIO.cleanup()
