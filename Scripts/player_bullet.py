from Globals import *
from blood import *
from enemyFollowDestroyed import *
class playerBullet(Actor):
	def __init__(self, startingx, startingy, velocity, mousePos):
		super().__init__(startingx, startingy,5, 5, (255, 255, 255), "../Images/bullet.png")
		self.rotation = math.atan2(mousePos[1] - self.rect.y, mousePos[0] - self.rect.x)
		#self.image = pygame.transform.rotate(self.imageS, math.degrees(self.rotation))
		self.speed = velocity
		self.life = 0
		self.backCounter = 0
		GroupManager.camera_group.add(self)
	def _update(self, player):
		if self.life <= 25:
			self.rect.x += math.cos(self.rotation) * self.speed
			self.rect.y += math.sin(self.rotation) * self.speed
			self.image.blit(self.imageS, (self.rect.x, self.rect.y))
			self.life += 1
			self.wall_collide = pygame.sprite.spritecollide(self, self.walls, False)
			self.enemy_collide = pygame.sprite.spritecollide(self, self.enemy, False)
			self.block_dest = pygame.sprite.spritecollide(self, self.Dblock, False)
			for col in self.enemy_collide:
				col.health -= player.playerInventory.getCurrentItem().damage
				print(player.playerInventory.getCurrentItem().name)
				#put blood tiles here?
				col.rect.x -= math.cos(col.rotation) * col.speed * 2
				if col.name == "Follow":
					blood = BloodStain(self.rect.x, self.rect.y)
					GroupManager.blood_sprite.add(blood)
				col.rect.y -= math.sin(col.rotation) * col.speed * 2

				self.kill()
			for col in self.wall_collide:
				self.kill()
			for col in self.block_dest:
				col.health -= player.playerInventory.getCurrentItem().damage

		else:
			self.kill()
