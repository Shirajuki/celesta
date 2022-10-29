import numpy as np
import math
import pygame

class Tile:
	__x = .0
	__y = .0
	__width = .0
	__height = .0
	__color = 0
	__image = pygame.image.load("agent.png")

	def __init__(self, x, y, width, height, color) -> None:
		self.__x = x
		self.__y = y
		self.__width = width
		self.__height = height
		self.__color = color

	def draw(self, gameDisplay, scroll) -> None:
		# gameDisplay.blit(self.__image, (self.__x, self.__y))
		pygame.draw.rect(gameDisplay, self.__color, pygame.Rect(self.__x*50 + scroll["x"], self.__y*50 + scroll["y"], self.__width, self.__height))


if __name__ == "__main__":
	t = Tile()

