#!/bin/sh

var=$( cat /home/pi/music/play_entry.txt )

if [ $var = "0" ]
then
   echo "sudo aplay /home/pi/music/welcome2.wav"
else
   echo "sudo aplay /home/pi/music/access_denied.wav"
fi
