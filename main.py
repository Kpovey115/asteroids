import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

from constants import *

def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # setting up game 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    

    #groups

    updatableGroup = pygame.sprite.Group()
    drawableGroup = pygame.sprite.Group()
    asteroidGroup = pygame.sprite.Group()
    shotGroup = pygame.sprite.Group()

   # asteroid / asteroid field logic
    Asteroid.containers = (asteroidGroup, updatableGroup, drawableGroup)
    AsteroidField.containers = updatableGroup
    asteroid_field = AsteroidField()

    # player logic
    Player.containers = (updatableGroup, drawableGroup)
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)

    #shot/bullet logic
    Shot.containers = (shotGroup, updatableGroup,drawableGroup)
    

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



        for updatableItem in updatableGroup:
            updatableItem.update(dt)
            
        
        for asteroidItem in asteroidGroup:

            if asteroidItem.collision(player):
                print("Game Over!")
                sys.exit()

        screen.fill("black")

        for drawableItem in drawableGroup:
            drawableItem.draw(screen)
    
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        player.shotTimer -= dt

if __name__ == "__main__":
    main()
    
