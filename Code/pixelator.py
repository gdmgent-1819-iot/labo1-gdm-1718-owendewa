from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()
while True:
	sense.clear()
	for x in range(8):
		for y in range(8):
			r = randint(0,255)
			g = randint(0,255)
			b = randint(0,255)
			sense.set_pixel(y,x,r,g,b)
			if y !=0:
				sense.set_pixel(y-1,x,0,0,0)
			if y == 0 and x!=0:
				sense.set_pixel(7,x-1,0,0,0)
			time.sleep(0.05)
			

			
		


