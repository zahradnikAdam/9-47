import random

import pygame

from settings import COIN_SIZE, HEIGHT, WIDTH, YELLOW


class Coin:
	def __init__(self):
		self.size = COIN_SIZE
		self.x = 0
		self.y = 0
		self.respawn()

	def respawn(self):
		self.x = random.randint(0, WIDTH - self.size)
		self.y = random.randint(40, HEIGHT - self.size)

	def get_rect(self):
		return pygame.Rect(self.x, self.y, self.size, self.size)

	def draw(self, screen):
		pygame.draw.ellipse(screen, YELLOW, self.get_rect())
