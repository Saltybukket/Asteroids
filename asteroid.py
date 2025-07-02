from circleshape import *
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        #spawn 2 new asteroids otherwise:
        random_angle = random.uniform(20, 50)
        
        first_angle = self.velocity.rotate(random_angle)
        second_angle = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        first_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_new_asteroid.velocity = first_angle * 1.2
        second_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_new_asteroid.velocity = second_angle * 1.2