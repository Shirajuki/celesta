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
                if platform_type == ".": # Normal block
                    tiles.append(Tile(x,y,50,50,(255,0,0)))
                elif platform_type == "x":
                    tiles.append(Tile(x,y,50,50,(255,255,0)))
        self.__tiles = tiles

    def is_colliding(self, x: int=0, y: int=0) -> bool:
        y = int(y/50)
        x = int(x/50)
        try:
            col = self.__field[y][x] 
            if col == ".": 
                return False
            elif col == "x":
                return True
        except:
            return False

    def get_field(self) -> np.ndarray: 
        return self.__tiles

if __name__ == "__main__":
    f = Field()

