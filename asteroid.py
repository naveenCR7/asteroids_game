import pygame, random
from circleshape import CircleShape

class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

        # Add self to any containers specified
        for group in self.containers:
            group.add(self)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    
    def split(self):
        # Always remove this asteroid
        self.kill()

        # If it's already the smallest size, don't split
        from constants import ASTEROID_MIN_RADIUS
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Create two new directions rotated off the original velocity
        random_angle = random.uniform(20, 50)

        direction1 = self.velocity.rotate(random_angle) * 1.2
        direction2 = self.velocity.rotate(-random_angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        from asteroid import Asteroid  # import here to avoid circular import issues

        # Spawn the two new asteroids at this asteroid's position
        Asteroid(self.position.x, self.position.y, new_radius).velocity = direction1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = direction2


    
