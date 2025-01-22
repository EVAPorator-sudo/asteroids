import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
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
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	asteroidfield = AsteroidField()
	player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)
	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		for i in updatable:
			i.update(dt)
		for i in drawable:
			i.draw(screen)
		pygame.display.flip()
		dt = Clock.tick(120) /1000

if __name__ == "__main__":
	main()
