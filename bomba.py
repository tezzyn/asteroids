import pygame
from circleshape import CircleShape

class Bomb(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, 10)
        self.exploded = False
        self.explosion_radius = 0
        self.explosion_max_radius = 120
        self.explosion_duration = 0.4  # seconds
        self.explosion_timer = 0

    def update(self, dt):
        if not self.exploded:
            self.position += self.velocity * dt
            # Example: explode after slowing down or on collision
            if self.velocity.length() < 10:  # or another condition
                self.explode()
        else:
            self.explosion_timer += dt
            self.explosion_radius = (self.explosion_timer / self.explosion_duration) * self.explosion_max_radius
            if self.explosion_timer >= self.explosion_duration:
                self.kill()  # Remove bomb after explosion

    def explode(self):
        self.exploded = True
        self.explosion_timer = 0
        self.explosion_radius = 0
        self.velocity = pygame.Vector2(0, 0)
        self.radius = self.explosion_max_radius  # For collision

    def draw(self, screen):
        if not self.exploded:
            pygame.draw.circle(screen, (255, 0, 0), self.position, 10)
        else:
            pygame.draw.circle(screen, (255, 200, 0), self.position, int(self.explosion_radius), 4)