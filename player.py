


from circleshape import *
from constants import *
from bullet import *


class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)

    self.rotation = 0
    self.timer = 0


  # in the player class
  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]


  def draw(self, screen):
    pygame.draw.polygon(screen, "white", self.triangle(), 2)

  def rotate(self, dt):
    self.rotation += PLAYER_TURN_SPEED * dt
    

  def update(self, dt):

    if self.position.x < 0:
      self.position.x = SCREEN_WIDTH

    if self.position.x > SCREEN_WIDTH:
      self.position.x = 0
    
    if self.position.y < 0:
      self.position.y = SCREEN_HEIGHT
    
    if self.position.y > SCREEN_HEIGHT:
      self.position.y = 0


    self.timer -= dt 

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
       
      shot = self.shoot()


    if keys[pygame.K_b]:
      self.boost(dt)
         
    if keys[pygame.K_a]:
        self.rotate(-dt)
        
        
    if keys[pygame.K_d]:
        self.rotate(dt)


    if keys[pygame.K_w]:
        self.move(dt)

    if keys[pygame.K_s]:
        self.move(-dt)
  

  def move(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt

  def shoot(self):
    if self.timer > 0:
      return
    self.timer = PLAYER_SHOOT_COOLDOWN
    
    #print("pew pew")
    bullet = Shot(self.position.x, self.position.y)
    fire = pygame.Vector2(0,1).rotate(self.rotation)
    bullet.velocity += fire * PLAYER_SHOOT_SPEED

    return bullet
    
  
  def boost(self, dt):
    boosty = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += boosty * PLAYER_BOOST_SPEED * dt

  def lives(self):
    self.life = 3
    return self.life
  
 
