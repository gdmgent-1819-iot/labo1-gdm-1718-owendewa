#imports
from sense_hat import SenseHat
from random import randint
import time
sense = SenseHat()

x = 1
#creating a nendless while loop
while True:
	#Generating two random colors
	randomcolor = (randint(0,255),randint(0,255),randint(0,255))
	randomcolor2 = (randint(0,255),randint(0,255),randint(0,255))

	#Show the message 'Hello! we are New Media Development :|' on the
	#sense hat and give the baclground the first generated color and the
	#text the second generated color with a scroll speed of 0.1
	
	sense.show_message("Hello! we are New Media Development :|", 
	text_colour=randomcolor, back_colour=randomcolor2, scroll_speed = 0.1)
	
	
