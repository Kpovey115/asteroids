from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __int__(self, x, y, radius):
   
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2 )

    def update(self, dt):
        self.position += self.velocity * dt