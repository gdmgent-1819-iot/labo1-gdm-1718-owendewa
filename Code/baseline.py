from sense_hat import SenseHat
from random import randint
import time
sense = SenseHat()

x = 1
while True:
	randomcolor = (randint(0,255),randint(0,255),randint(0,255))
	randomcolor2 = (randint(0,255),randint(0,255),randint(0,255))
	sense.show_message("Hello! we are New Media Development :|", 
	text_colour=randomcolor, back_colour=randomcolor2, scroll_speed = 0.1)
	
	
