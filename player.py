import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
	def __init__(self,x, y, shots):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shots = shots
		self.shot_timer = 0

		# in the player class
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def update(self, dt):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.rotate(0 - dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt, "forward")
		if keys[pygame.K_s]:
			self.move(dt, "backward")
		if keys[pygame.K_SPACE]:
			if self.shot_timer < 0:
				self.shoot()
		self.shot_timer -= dt

	def move(self,dt, direction):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		if direction == "forward":
			self.position += forward * PLAYER_SPEED * dt
		elif direction == "backward":
			self.position -= forward * PLAYER_SPEED * dt
	
	def shoot(self):
		shot = Shot(self.position.x, self.position.y)
		shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
		self.shots.add(shot)
		self.shot_timer = 0.3