import sys
import pygame, circleshape, asteroid
from constants import *
from player import *
from asteroidfield import *
from shot import Shot
#from circleshape

def main():

  pygame.init()

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  print("Starting Asteroids!")

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  asteroid_field = AsteroidField()

  Player.containers = (updatable, drawable, shots)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


  

  dt = 0


  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    updatable.update(dt)

    for item in asteroids:

      if item.collide(player):
        #print("Game Over!")
        sys.exit("Game Over!")

    screen.fill("black")

    for items in drawable:
      items.draw(screen)

    

    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

    









    


if __name__ == "__main__":
     main()
