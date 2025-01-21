import pygame
from constants import * 
pygame.init()

def main():
	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
        		return
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while(True):
		screen.fill((0,0,0))
		pygame.display.flip()

if __name__ == "__main__":
	main()
