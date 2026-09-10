import pygame
from settings import (
   WIDTH,
   HEIGHT,
   PLAYER_SIZE,
   PLAYER_SPEED,
   BLUE
)

class Player:
   def __init__(self):
       self.x = WIDTH // 2
       self.y = HEIGHT // 2
       self.size = PLAYER_SIZE
       self.speed = PLAYER_SPEED
   def move(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_w] or keys[pygame.K_UP]:
           self.y -= self.speed
       if keys[pygame.K_s] or keys[pygame.K_DOWN]:
           self.y += self.speed
       if keys[pygame.K_a] or keys[pygame.K_LEFT]:
           self.x -= self.speed
       if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
           self.x += self.speed
       # Hráč zůstane uvnitř obrazovky
       self.x = max(0, min(WIDTH - self.size, self.x))
       self.y = max(40, min(HEIGHT - self.size, self.y))
   def get_rect(self):
       return pygame.Rect(
           self.x,
           self.y,
           self.size,
           self.size
       )
   def draw(self, screen):
       pygame.draw.rect(
           screen,
           BLUE,
           self.get_rect()
       )