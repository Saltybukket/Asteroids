#constants must be in first line for pygame to access
#imports all as is -> with "import constants" -> would need constants.<CONSTANT> to access
from constants import *     
import pygame


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    game_clock = pygame.time.Clock()
    dt = 0      #delta time
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))     #Display dimensions as touple
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        pygame.display.flip()       #need pygame.display.flip() instead of screen.flip() -> not a surface method
        
        dt = game_clock.tick(60) / 1000         #wait 1/60 sec  | retuns time since last call (delta_time)
    
if __name__ == "__main__":
    main()