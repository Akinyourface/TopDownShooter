from Globals import *
from Weapon import *

class RocketLauncher(Weapon):
	def __init__(self):
		super().__init__("Rocket Launcher", 250, 5, "../Images/rocketInventory.png")
		self.name = "RocketLauncher"
