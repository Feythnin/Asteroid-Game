import pygame
import random
from constants import *
from circleshape import CircleShape
from logger import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(self.position.x, self.position.y)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity  *dt)
    
    def split(self, dt):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return True
        else:
            log_event("asteroid_split")
            random.uniform(19, 51)
            new_vector = self.velocity.rotate(dt)
            opp_vector = self.velocity.rotate(-dt)
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = new_vector * 1.2

            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = opp_vector * 1.2

            