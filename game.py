import pygame
import sys
from player import Player
from coin import Coin
from settings import (
   WIDTH,
   HEIGHT,
   FPS,
   GAME_TIME,
   BLACK,
   WHITE
)

class Game:
   def __init__(self):
       pygame.init()
       self.screen = pygame.display.set_mode(
           (WIDTH, HEIGHT)
       )
       pygame.display.set_caption("Chyť minci")
       self.clock = pygame.time.Clock()
       self.font = pygame.font.Font(None, 36)
       self.big_font = pygame.font.Font(None, 70)
       self.player = Player()
       self.coin = Coin()
       self.score = 0
       self.start_time = pygame.time.get_ticks()
       self.running = True
       self.game_over = False
   def handle_events(self):
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               self.running = False
   def update(self):
       if self.game_over:
           return
       self.player.move()
       if self.player.get_rect().colliderect(
           self.coin.get_rect()
       ):
           self.score += 1
           self.coin.respawn()
       elapsed = (
           pygame.time.get_ticks() - self.start_time
       ) // 1000
       if elapsed >= GAME_TIME:
           self.game_over = True
   def draw(self):
       self.screen.fill(BLACK)
       if not self.game_over:
           self.player.draw(self.screen)
           self.coin.draw(self.screen)
           self.draw_hud()
       else:
           self.draw_game_over()
       pygame.display.flip()
   def draw_hud(self):
       elapsed = (
           pygame.time.get_ticks() - self.start_time
       ) // 1000
       remaining = max(0, GAME_TIME - elapsed)
       score_text = self.font.render(
           f"Skóre: {self.score}",
           True,
           WHITE
       )
       time_text = self.font.render(
           f"Čas: {remaining}",
           True,
           WHITE
       )
       self.screen.blit(
           score_text,
           (20, 10)
       )
       self.screen.blit(
           time_text,
           (WIDTH - 130, 10)
       )
   def draw_game_over(self):
       title = self.big_font.render(
           "KONEC HRY!",
           True,
           WHITE
       )
       score = self.font.render(
           f"Skóre: {self.score}",
           True,
           WHITE
       )
       restart = self.font.render(
           "Stiskni R pro novou hru",
           True,
           WHITE
       )
       self.screen.blit(
           title,
           (
               WIDTH // 2 - title.get_width() // 2,
               200
           )
       )
       self.screen.blit(
           score,
           (
               WIDTH // 2 - score.get_width() // 2,
               290
           )
       )
       self.screen.blit(
           restart,
           (
               WIDTH // 2 - restart.get_width() // 2,
               350
           )
       )
   def restart(self):
       self.player = Player()
       self.coin = Coin()
       self.score = 0
       self.start_time = pygame.time.get_ticks()
       self.game_over = False
   def run(self):
       while self.running:
           self.handle_events()
           # Restart po konci hry
           if self.game_over:
               keys = pygame.key.get_pressed()
               if keys[pygame.K_r]:
                   self.restart()
           self.update()
           self.draw()
           self.clock.tick(FPS)
       pygame.quit()
       sys.exit()