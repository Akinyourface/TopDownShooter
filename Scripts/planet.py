from Globals import *
from random import randint



class Planet(Actor):
	def __init__(self, x, y, speed):
		 super().__init__(x, y, 60, 60, (255, 0, 0), "../Images/planet.png")
		 self.RandRot = randint(0, 360)
		 self.image = pygame.transform.rotate(self.imageS, self.RandRot)
		 self.movspeed = speed
		 self.posX = x

	def update(self):

		if self.rect.y <= -60:
			self.posX = 480
			self.rect.x = randint(60, 640 - 60)
			self.image = pygame.transform.rotate(self.imageS, randint(0, 360))
		else:
			self.posX -= self.movspeed

		self.rect.y = int(self.posX)
