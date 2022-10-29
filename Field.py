"""
Platform handles collision checks
"""

import numpy as np
from Tile import Tile


class Field:
    def __init__(self, map) -> None:
        self.__field = [x.strip() for x in open(map).readlines() if x != ""]
        tiles = []
        for y in range(len(self.__field)):
            for x in range(len(self.__field[y])):
                platform_type = self.__field[y][x]
                if platform_type == ".":
                    tiles.append(Tile(x,y,50,50,(255,0,0)))
                elif platform_type == "x":
                    tiles.append(Tile(x,y,50,50,(255,255,0)))
                elif platform_type == "#":
                    tiles.append(Tile(x,y,50,50,(255,255,255)))
                elif platform_type == "+":
                    tiles.append(Tile(x,y,50,50,(0,0,0)))
        self.__tiles = tiles

    # def check_conditions(self, x: int=0, y: int=0) -> bool:
    #     y = int(y/50)
    #     x = int(x/50)
    #     for xi in [x-1, x, x+1]:
    #         for yi in [y-1, y, y+1]:
    #             try:
    #                 col = self.__field[yi][xi] 
    #                 if col == ".": 
    #                     return "Free"
    #                 elif col == "x":
    #                     return "Wall"
    #                 elif col == "+":
    #                     return "Bomb"
    #             except:
    #                 return False
    
    # def is_floor(self, x: int=0, y: int=0) -> bool:
    #     x = int(x/50)
    #     y = int(y/50)
    #     try:
    #         col = self.__field[y][x] 
    #         if col == "x":
    #             return True
    #         elif col == "+":
    #             return False
    #     except:
    #         return False
    
    # def is_wall(self, x: int=0, y: int=0) -> bool: 
    #     x = int(x/50)
    #     y = int(y/50)
    #     try:
    #         col = self.__field[y][x] 
    #         if col == "x":
    #             return True
    #         elif col == "+":
    #             return False
    #     except:
    #         return False

    # def is_bomb(self, x: int=0, y: int=0) -> bool:
    #     y = int(y/50)
    #     x = int(x/50)
    #     for xi in [x-1, x, x+1]:
    #         for yi in [y-1, y, y+1]:
    #             try:
    #                 col = self.__field[yi][xi] 
    #                 if col == "+":
    #                     return True
    #                 else: 
    #                     return False
    #             except:
    #                 return False

    def get_tiles(self) -> list: 
        return self.__tiles

    def get_field(self) -> list:
        return self.__field

if __name__ == "__main__":
    f = Field()

