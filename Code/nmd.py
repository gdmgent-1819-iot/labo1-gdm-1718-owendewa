from sense_hat import SenseHat
from random import randint
import time
sense = SenseHat()

x = 1
while x <= 1:
	randomcolor = (randint(0,255),randint(0,255),randint(0,255))
	sense.show_letter("N",randomcolor)
	time.sleep(1)
	sense.show_letter("M",randomcolor)
	time.sleep(1)
	sense.show_letter("D",randomcolor)
	time.sleep(2)


