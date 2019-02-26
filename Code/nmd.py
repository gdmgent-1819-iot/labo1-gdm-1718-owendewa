#imports
from sense_hat import SenseHat
from random import randint
import time
sense = SenseHat()

x = 1
# Creating an endless while loop
while x <= 1:
	# Generating a random color that wil be used for 
	# all three letter N,M,D as they display with each 
	# 1 second interval and at the end a 2 second interval
	randomcolor = (randint(0,255),randint(0,255),randint(0,255))
	sense.show_letter("N",randomcolor)
	time.sleep(1)
	sense.show_letter("M",randomcolor)
	time.sleep(1)
	sense.show_letter("D",randomcolor)
	time.sleep(2)


