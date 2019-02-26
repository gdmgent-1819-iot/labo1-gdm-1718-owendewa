#imports
from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()
#Creating endless while loop
while True:
	#Clearing the sense hat each new loop
	sense.clear()
	#Creating two for loops to cover all the sense hat lights
	for x in range(8):
		for y in range(8):
			# Generating 3 randoom RGB values for each light
			r = randint(0,255)
			g = randint(0,255)
			b = randint(0,255)
			# Give each new pixel the random generated RGB value
			sense.set_pixel(y,x,r,g,b)
			# If the horizontal pixel is not 0 give the pixel 
			# before this one a value of 0
			if y !=0:
				sense.set_pixel(y-1,x,0,0,0)
			# If the horizontal light is 0 and the vertical row isn't 0
			# Give the last light on the row before a value of 0
			if y == 0 and x!=0:
				sense.set_pixel(7,x-1,0,0,0)
			time.sleep(0.5)
			

			
		


