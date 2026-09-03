from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS

from logger import log_event

import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "WHITE", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, angle)*1.2
            new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -angle)*1.2
