import pygame
import random
from constants import *
from circleshape import CircleShape
class Asteroid(CircleShape):
	def __init__(self, x, y ,radius, asteroids):
		super().__init__(x, y, radius)
		self.asteroids = asteroids

	def draw(self, screen):
		pygame.draw.circle(screen, "white",self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			random_angle = random.uniform(20, 50)
			V1 = self.velocity.rotate(random_angle) * 1.2
			V2 = self.velocity.rotate(0 - random_angle) *1.2
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, self.asteroids) #need to add V1 and V2
			asteroid1.velocity = V1
			self.asteroids.add(asteroid1)
			asteroid2 = Asteroid(self.position.x, self.position.y, new_radius,  self.asteroids )
			asteroid2.velocity = V2
			self.asteroids.add(asteroid2)
