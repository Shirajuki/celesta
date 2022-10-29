"""
Agent class handles the properties, 
"""
import numpy as np
import math
import pygame

class Agent:
	__x = 60
	__y = 60
	__width = 50
	__height = 50
	__vx = .0
	__vy = .0
	__g = .1
	__ay = __g
	__speed = 2
	__jump_height = 3
	__dash_distance = 4
	__jump_limit = 2
	__current_jumps = 0

	__HP = 1
	
	__movement = {
		"up": False,
		"down": False,
		"left": False,
		"right": False,
		"jump": False,
		"dash": False,
	}
	__facing = "right"
	__image = pygame.image.load("agent.png")
	__image = pygame.transform.scale(__image, (__width, __height))

	def __init__(self) -> None:
		pass

	def add_life(self) -> None: 
		self.__HP += 1

	def kill_life(self) -> None: 
		self.__HP -= 1
		
	def move(self, key: str="down") -> None:
		self.__movement[key] = True
	
	def update(self) -> None:
		## Gravitation
		self.__vy += self.__ay

		## Collision

		if self.__movement["right"]:
			self.__vx = self.__speed
			self.change_facing("right")
			self.__facing = 'right'
		if self.__movement["left"]:
			self.__vx = -self.__speed
			self.change_facing("left")
			self.__facing = "left"
		if self.__movement["down"]:
			self.__vy = self.__speed
		if self.__movement["up"]:
			self.__vy = -self.__speed
		if self.__movement['jump']:
			self.__vy = -self.__jump_height
		if self.__movement['dash']:
			if self.__facing == 'left':
				self.__vx = -self.__dash_distance
			else: 
				self.__vx = self.__dash_distance
		
		## Movement
		self.__x += self.__vx
		self.__y += self.__vy

		self.reset()
		
	def draw(self, gameDisplay, scroll) -> None:
		gameDisplay.blit(self.__image, (200, 200))#self.__x + scroll["x"], self.__y + scroll["y"]))

	def change_facing(self, facing) -> None:
		if self.__facing != facing:
			self.__image = pygame.transform.flip(self.__image, True, False)

	def get_location(self) -> tuple: 
		return self.__x, self.__y
	
	def get_movement(self) -> object:
		return self.__movement
	
	def get_facing(self) -> str:
		return self.__facing

	def reset(self) -> None:
		self.__movement = {
			"up": False,
			"down": False,
			"left": False,
			"right": False,
			"jump": False,
			"dash": False,
		}
		self.__vx = 0

if __name__ == "__main__":
	a = Agent()

