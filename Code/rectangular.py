#imports
from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

#Creating a nendless loop
while True:
	#Generate colors for rectangular
	r=(randint(0,255),randint(0,255),randint(0,255))
	b=(0,0,0)
	#Shaping the rectangulars
	r1 = [
		r,b,b,b,b,b,b,b,
		b,b,b,b,b,b,b,b,
		b,b,b,b,b,b,b,b,
		b,b,b,b,b,b,b,b,
		b,b,b,b,b,b,b,b,
		b,b,b,b,b,b,b,b,
		b,b,b,b,b,b,b,b,
		b,b,b,b,b,b,b,b,
	]
	r2 = [
		r,r,r,r,b,b,b,b,
		r,b,b,r,b,b,b,b,
		r,b,b,r,b,b,b,b,
		r,r,r,r,b,b,b,b,
		b,b,b,b,b,b,b,b,
		b,b,b,b,b,b,b,b,
		b,b,b,b,b,b,b,b,
		b,b,b,b,b,b,b,b,
	]
	r3 = [
		r,r,r,r,r,r,b,b,
		r,b,b,b,b,r,b,b,
		r,b,b,b,b,r,b,b,
		r,b,b,b,b,r,b,b,
		r,b,b,b,b,r,b,b,
		r,r,r,r,r,r,b,b,
		b,b,b,b,b,b,b,b,
		b,b,b,b,b,b,b,b,
	]
	r4 = [
		r,r,r,r,r,r,r,r,
		r,b,b,b,b,b,b,r,
		r,b,b,b,b,b,b,r,
		r,b,b,b,b,b,b,r,
		r,b,b,b,b,b,b,r,
		r,b,b,b,b,b,b,r,
		r,b,b,b,b,b,b,r,
		r,r,r,r,r,r,r,r,
	]
	# Displaying the different ractangulars on the sensehat
	# with a inerval of .5 seconds
	sense.set_pixels(r1)
	time.sleep(0.5)
	sense.set_pixels(r2)
	time.sleep(0.5)
	sense.set_pixels(r3)
	time.sleep(0.5)
	sense.set_pixels(r4)
	time.sleep(0.5)
	sense.set_pixels(r3)
	time.sleep(0.5)
	sense.set_pixels(r2)
	time.sleep(0.5)
	

	
