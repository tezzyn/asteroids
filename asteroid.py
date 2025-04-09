import pygame
from constants import *





from circleshape import *


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        


        super().__init__(self.x, self.y, self.radius)
        self.velocity = 0

    
    

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), 2)

    def update(self, dt):
        self.position += self.velocity * dt


    