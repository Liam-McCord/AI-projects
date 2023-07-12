This code was made to function with a very specific setup between a raspberry pi and my computer. Currently the raspberry pi part of the code is not on this repo as it is difficult to copy over. 

The raspi-communicator program should be run BEFORE the hand-tracker program, and they both run simultaneously as that was the best solution I found to both connect to the pi and track the hand simultaneously. A camera is needed for the hand tracking section, and the calibration is to determine the size of your hand so it can be used as a reference point to tell how close it is to the camera. This stops the program from thinking you've closed your hand as you move it further away. For the best results, your palm should be facing the camera and entirely within frame.

- Liam