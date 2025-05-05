import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot
from bomba import Bomb


def main():

  pygame.init()

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  print("Starting Asteroids!")

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  bullets = pygame.sprite.Group()
  bomba = pygame.sprite.Group()

  
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  asteroid_field = AsteroidField()

  Player.containers = (updatable, drawable, bullets, bomba)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


  Shot.containers = (updatable, drawable, bullets)

  Bomb.containers = (updatable, drawable, bomba)

  # boom = Bomb()


  bg_img = pygame.image.load("img/beautiful_space_view-wallpaper-1280x720.jpg")

  score = 0
  
  bg_color = (0,0,0)


  dt = 0

  lifes = player.lives()


  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    updatable.update(dt)

    for item in asteroids:

      if item.collide(player):
        lifes -= 1
        if lifes <= 0: 
          print(f"score = {score}")
          sys.exit("Game Over!")
        else:
          player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        

    screen.fill(bg_color)
    screen.blit(bg_img, (0,0))
    
    

    for items in drawable:
      items.draw(screen)

    for asteroid in asteroids:
      for rounds in bullets:
        if rounds.collide(asteroid):
          score += 1
          
          rounds.kill()
          asteroid.split()

    for asteroid in asteroids:
      for booms in bomba:
        if booms.collide(asteroid):
          score += 1
          
          booms.kill()
          asteroid.split()
          

    

    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

    









    


if __name__ == "__main__":
     main()
