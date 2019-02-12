#!/usr/local/bin/bash

import os

os.system("source ~/.profile")
os.system("workon cv")

os.system("python /home/pi/pi-deep-learning/pi_deep_learning.py --prototxt /home/pi/pi-deep-learning/models/bvlc_googlenet.prototxt --model /home/pi/pi-deep-learning/models/bvlc_googlenet.caffemodel --labels /home/pi/pi-deep-learning/synset_words.txt --image /home/pi/pi-deep-learning/images/image.jpg > /home/pi/foo.txt")
