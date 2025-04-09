import pygame, circleshape
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
#from circleshape

def main():

  pygame.init()



  print("Starting Asteroids!")

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroid = pygame.sptite.Group()

  Player.containers = (updatable, drawable)

  Asteroid.containers = (asteroid, updatable, drawable)
  

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  AsteroidField()

  dt = 0

  updatable.add(player)
  updatable.add(AsteroidField)




  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    updatable.update(dt)
       
    screen.fill("black")

    for items in drawable:
      items.draw(screen)



    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

    









    


if __name__ == "__main__":
     main()
