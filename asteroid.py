import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if ASTEROID_MIN_RADIUS >= self.radius:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            vel_one = self.velocity.rotate(random_angle)
            vel_two = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_one = Asteroid(self.position.x, self.position.y, new_radius)
            new_two = Asteroid(self.position.x, self.position.y, new_radius)
            new_one.velocity = vel_one * 1.2
            new_two.velocity = vel_two * 1.2