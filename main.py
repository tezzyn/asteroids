import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot


def main():

  pygame.init()

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  print("Starting Asteroids!")

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  bullets = pygame.sprite.Group()

  

  
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  asteroid_field = AsteroidField()

  Player.containers = (updatable, drawable, bullets)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  Shot.containers = (updatable, drawable, bullets)



  
  

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

    for asteroid in asteroids:
      for rounds in bullets:
        if rounds.collide(asteroid):
          rounds.kill()
          asteroid.split()
          

    

    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

    









    


if __name__ == "__main__":
     main()
