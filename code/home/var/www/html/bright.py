import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
my_pwm=GPIO.PWM(17,100)
my_pwm.start(0)
while(1):
	bright=input("How bright Do you Want the LED ? (1 - 6)")
	my_pwm.ChangeDutyCycle(2**bright)
my_pwm.stop()
GPIO.cleanup()

