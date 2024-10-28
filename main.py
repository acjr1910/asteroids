import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  
  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  while True:
     for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
     for u in updatable:
      u.update(dt)

     screen.fill("#000000")

     for d in drawable:
      d.draw(screen)
     
     pygame.display.flip()

     dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()