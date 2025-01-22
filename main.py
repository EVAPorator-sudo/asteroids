import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

pygame.init()

def main():
	Clock = pygame.time.Clock()
	dt = 0
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	Shot.containers = (shots, updatable, drawable)
	asteroidfield = AsteroidField()
	player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2, shots)
	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		for i in updatable:
			i.update(dt)
		for i in asteroids:
			if player.collision_check(i) == True:
				print("Game Over!")
				sys.exit()
		for i in drawable:
			i.draw(screen)
		pygame.display.flip()
		dt = Clock.tick(120) /1000

if __name__ == "__main__":
	main()
