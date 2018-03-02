from Globals import *
from Weapon import *


class AssaultRifle(Weapon):
	def __init__(self):
		super().__init__("Assault Weapon", 50, 150, "../Images/rifleInventory.png")
		self.name = "AssaultRifle"
