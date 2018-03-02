from Globals import *

class Enemybullet(Actor):
	def __init__(self, startingx, startingy, velocity, player):
		super().__init__(startingx, startingy,5, 5, (255, 255, 255), "../Images/bullet.png")
		self.rotation = math.atan2(player.rect.y - self.rect.y, player.rect.x - self.rect.x)
		self.image = pygame.transform.rotate(self.imageS, math.degrees(self.rotation))
		self.speed = velocity
		self.life = 0
		GroupManager.camera_group.add(self)
	def _update(self, player):
		if self.life <= 50:
			self.rect.x += math.cos(self.rotation) * self.speed
			self.rect.y += math.sin(self.rotation) * self.speed
			self.image.blit(self.imageS, (self.rect.x, self.rect.y))
			self.life += 1

		else:
			self.kill()
		self.wall_collide = pygame.sprite.spritecollide(self, self.walls, False)
		for col in self.wall_collide:
			self.kill()
