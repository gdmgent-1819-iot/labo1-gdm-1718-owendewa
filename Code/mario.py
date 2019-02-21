from sense_hat import SenseHat

sense = SenseHat()
r = (255,0,0)
b = (0,0,255)
w = (255,255,255)
x = (139,69,19)
s = (244,164,96)
y = (0,0,0)
z = (255,255,0)
Mdown = [
	y,y,y,r,r,r,r,y,
	y,y,y,r,r,r,r,r,
	y,y,x,s,x,y,s,y,
	y,y,x,s,s,x,x,s,
	y,y,y,x,s,s,s,y,
	y,r,r,z,b,b,r,y,
	w,y,b,b,b,b,y,w,
	y,y,x,y,y,y,x,y,
]
Mup = [
	y,y,x,s,x,y,s,y,
	y,y,x,s,s,x,x,s,
	y,y,y,x,s,s,s,y,
	y,r,r,z,b,b,r,y,
	w,y,b,b,b,b,y,w,
	y,y,x,y,y,y,x,y,
	y,y,y,y,y,y,y,y,
	y,y,y,y,y,y,y,y,
]

def up():
	sense.set_pixels(Mup)

def down():
	sense.set_pixels(Mdown)
	
sense.stick.direction_up = up
sense.stick.direction_down = down
sense.stick.direction_middle = sense.clear

while True:
	
	pass
