from Globals import *

class Inventory:
	def __init__(self):
		self.listofItems = []
		self.currentItem = 0


	def addToInventory(self, name):
		if name in self.listofItems:
			pass
			#print("you already have this item in your inventory")
		else:
			self.listofItems.append(name)
	def getCurrentItem(self):
		return self.listofItems[self.currentItem]

	def setCurrentItem(self, id):
		if id == "Pistol":
			self.currentItem = 0
		if id == "Assault":
			self.currentItem = 1
		if id == "Rocket":
			self.currentItem = 2
