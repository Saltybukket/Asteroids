import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)   
         #takes (<screen object>, <color>, <list of coordinates>, <line width>)
        
    def update(self, dt):
        # sub-classes must override
        pass
    
    def check_collision(self, other):
        distance = self.position.distance_to(other.position)    #position is already pygame.Vector2
        return self.radius + other.radius >= distance
