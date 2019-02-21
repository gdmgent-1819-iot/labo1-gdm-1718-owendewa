from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

while True:
	for x in range (8):
		for y in range(8):
			n = (randint(0,1))
			if n == 0:
				sense.set_pixel(x,y,0,0,0)
			else: 
				sense.set_pixel(x,y,255,255,255)
	time.sleep(2)

	
