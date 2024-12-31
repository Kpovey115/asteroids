from circleshape import CircleShape
import random
import pygame
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2 )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        randomAngle = random.uniform(20, 50)

        newVector1 = self.velocity.rotate(randomAngle)
        newVector2 = self.velocity.rotate(-randomAngle)

        newAsteroidRadius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, newAsteroidRadius)
        asteroid2 = Asteroid(self.position.x, self.position.y, newAsteroidRadius)

        asteroid1.velocity = newVector1 * 1.2
        asteroid2.velocity = newVector2 * 1.2
