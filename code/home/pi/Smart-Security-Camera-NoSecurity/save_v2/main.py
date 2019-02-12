import cv2
import sys
from mail import sendEmail
from flask import Flask, render_template, Response
from camera import VideoCamera
import time
import threading
import RPi.GPIO as GPIO
import subprocess
import os

email_update_interval = 600 # sends an email only once in this time interval
video_camera = VideoCamera(flip=True) # creates a camera object, flip vertically
object_classifier = cv2.CascadeClassifier("models/upperbody_recognition_model.xml") # an opencv classifier

# u=commands.getoutput('python dimLED.py')
# p=subprocess.call('sudo python /home/pi/Smart-Security-Camera/dimLED.py')
# os.system("sudo python /home/pi/Smart-Security-Camera/dimLED.py")
# os.system("gpio -g mode 4 out")
# os.system("gpio -g write 4 1")

# wiringpi.wiringPiSetup()
# wiringpi.wiringPiSetupGpio()
# wiringpi.wiringPiSetupPhys()
# wiringpi.digitalWrite(4, 1)

# App Globals (do not edit)
app = Flask(__name__)
last_epoch = 0

def check_for_objects():
	global last_epoch
	while True:
		try:
			frame, found_obj = video_camera.get_object(object_classifier)
			if found_obj and (time.time() - last_epoch) > email_update_interval:
				last_epoch = time.time()
				print("Sending email...")
				os.system("sudo pkill -f dimLED.py")
				os.system("gpio -g write 4 0")
				os.system("sudo python /home/pi/Smart-Security-Camera/dimLED.py &")
				sendEmail(frame)
				print("done!")
		except:
			print("Error sending email: ", sys.exc_info()[0])




@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    t = threading.Thread(target=check_for_objects, args=())
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', debug=False)