from Globals import *
from Weapon import *

class SimplePistol(Weapon):
	def __init__(self):
		super().__init__("Simple Pistol", 5, 150, "../Images/pistolInventory.png")
		self.name = "SimplePistol"
