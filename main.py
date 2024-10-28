import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Asteroid.containers = (asteroids, updatable, drawable)
  Shot.containers = (shots, updatable, drawable)
  AsteroidField.containers = updatable
  asteroid_field = AsteroidField()
  
  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  while True:
     for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
     for u in updatable:
      u.update(dt)

     for a in asteroids:
       if a.collides_with(player):
         print("Game over!")
         sys.exit()
       for shot in shots:
        if a.collides_with(shot):
            shot.kill()
            a.kill()
            a.split()

     screen.fill("#000000")

     for d in drawable:
      d.draw(screen)
     
     pygame.display.flip()

     dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()