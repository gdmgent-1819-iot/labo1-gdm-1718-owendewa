from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

while True:

	r=(randint(0,255),randint(0,255),randint(0,255))

	b=(0,0,0)

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
	

	
