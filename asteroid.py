import pygame, circleshape
from constants import *








class Asteroid(circleshape):


    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        


        super().__init__(self.x, self.y, self.radius)
        self.velocity = 0

    
    

    def draw(self, x, y, radius):
        pygame.draw.circle(x, y, radius=2)

    def update(self, dt):
        self.position += Asteroid.velocity * dt


    