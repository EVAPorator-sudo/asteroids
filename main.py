import pygame
from constants import *
from player import *
pygame.init()

def main():
	Clock = pygame.time.Clock()
	dt = 0
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)
	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		player.draw(screen)
		pygame.display.flip()
		dt = Clock.tick(120) /1000

if __name__ == "__main__":
	main()
