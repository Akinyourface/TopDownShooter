from Globals import *

class Door1(Actor):
	def __init__(self, x, y):
		super().__init__(x, y, 16, 16, (255, 255, 255), "../Images/door1.png")
