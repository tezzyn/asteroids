import pygame, circleshape
from constants import *
from player import *
#from circleshape

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

  player = Player(x= SCREEN_WIDTH / 2, y= SCREEN_HEIGHT / 2)

  while True:

    dt = clock.get_time() / 1000

    Player.update(dt)
    screen.fill("black")
  
    player.draw(screen)
    
    pygame.display.flip()
    
    
    clock.tick(60)

    

    









    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return


if __name__ == "__main__":
     main()
