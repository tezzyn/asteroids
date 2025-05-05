import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Bomb(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    
    

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 163, 26), self.position, SHOT_RADIUS*3, 4)

    def update(self, dt):
        self.position += self.velocity * dt