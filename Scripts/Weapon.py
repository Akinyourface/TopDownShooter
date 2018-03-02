from Globals import *

class Weapon:
	def __init__(self, name, damage, ammoCapacity, image):
		self.name = name
		self.damage = damage
		self.image = pygame.image.load(image)
		self.ammoCapacity = ammoCapacity
		self.currentAmmo = self.ammoCapacity
		self.name = "Undefined"
		self.imageWidth = 32
