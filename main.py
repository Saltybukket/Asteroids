#imports all as is -> with "import constants" -> would need constants.<CONSTANT> to access
from constants import * 
from player import *  
from asteroidfield import *  
import sys
import pygame


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    game_clock = pygame.time.Clock()
    dt = 0      #delta time
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))     #Display dimensions as touple
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    
    asteroid_field = AsteroidField()
    player_ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #==== Game Loop ====
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("> Game has been closed")
                return
            
        updatable.update(dt)      #updates all group elements
        screen.fill("black")
        
        for asteroid in asteroids:
            if player_ship.check_collision(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()   

        
                    
        
        
        for drawable_obj in drawable:
            drawable_obj.draw(screen)         #draws all group elements
        
        pygame.display.flip()       #need pygame.display.flip() instead of screen.flip() -> not a surface method

        dt = game_clock.tick(60) / 1000         #wait 1/60 sec  | retuns time since last call (delta_time)

    
if __name__ == "__main__":
    main()