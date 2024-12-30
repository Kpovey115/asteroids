import pygame

# circle shape will be the base class for the game, asteroids and the ship will be a circle
# it will also inherit from pygames sprites class

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()


        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius



    def draw(self, screen):
        # child classes will override
        pass


    def update(self, dt):
        #child classes will override
        pass
