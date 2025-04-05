import pygame
from constants import *

def main():

  pygame.init()

  #SCREEN_WIDTH = constants.SCREEN_WIDTH
  #SCREEN_HEIGHT = constants.SCREEN_HEIGHT

  #print("Starting Asteroids!")
  #print(f"Screen width: {SCREEN_WIDTH}")
  #print(f"Screen height: {SCREEN_HEIGHT}")

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()
  dt = 0


  while True:
    screen.fill("black")
    pygame.display.flip()

    clock.tick(60)

    dt = clock.get_time() / 1000








    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return


if __name__ == "__main__":
     main()
