#imports
from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()
#creating an endless while loop
while True:

	#Creating two for loops where foreach light on the 
	#sense hat a value is generated between 1 and 0
	#if this value is 1 give the light a color value of white
	#if not give it a color value of black
	for x in range (8):
		for y in range(8):
			n = (randint(0,1))
			if n == 0:
				sense.set_pixel(x,y,0,0,0)
			else: 
				sense.set_pixel(x,y,255,255,255)
	#give an interval of 2 seconds
	time.sleep(2)

	
