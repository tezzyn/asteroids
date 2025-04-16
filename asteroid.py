import pygame, random
from circleshape import CircleShape
from constants import *



class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    

    def draw(self, screen):


        polygon = [(self.position.x, self.position.y), (self.position.x+60, self.position.y+60), (self.position.x+self.radius, self.position.y)]
        #pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        pygame.draw.polygon(screen, "white", polygon, 2)


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            traj = random.uniform(20, 50)
            vec_1 = self.velocity.rotate(traj)
            vec_2 = self.velocity.rotate(-traj)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            split_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            split_asteroid1.velocity = vec_1
            split_asteroid2.velocity = vec_2


    