import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    # Initialize pygame
    pygame.init()

    # Set up screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # FPS control
    clock = pygame.time.Clock()
    dt = 0  # delta time in seconds

    # Create groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    # Register static containers
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (shots, updatables, drawables)
    
    # Create player in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatables.add(player)
    drawables.add(player)

    # Create asteroid spawner
    asteroid_field = AsteroidField()

            
    # Game loop
    while True:
        # Handle window close event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update all objects
        for obj in updatables:
            obj.update(dt)

        # Check for collision between player and any asteroid
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                return
            
        # Check for bullet–asteroid collisions
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()



        # Draw black screen
        screen.fill((0, 0, 0))
        
        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()  # Flip screen


        # Cap to 60 FPS, store delta time (in seconds)
        dt = clock.tick(60) / 1000

        # Uncomment to debug:
        # print(f"dt: {dt}")

if __name__ == "__main__":
    main()
