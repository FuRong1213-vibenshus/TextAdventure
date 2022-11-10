from Rooms import mainentrance, hauntedroom, skeletonroom
from Places import shadowfigure
import numpy as np
from .map import Map
from pathlib import Path
map_width = 3
map_height = 2
map_file = "map.txt"

place_class_dict = {"mainentrance": mainentrance.MainEntrance, 
                    "hauntedroom" : hauntedroom.HauntedRoom,
                    "shadowfigure": shadowfigure.ShadowFigure,
                    "skeletonroom": skeletonroom.SkeletonRoom}

class LoadMap:
    def __init__(self):
        self.game_map = Map()
        p = Path(__file__).with_name(map_file)
        with p.open('r') as f:
            self.entity_list = f.read().split()
        f.close()
        self.build_map()
        self.print_map()
    
    def print_map(self):
        print(self.game_map)
    
    def add_neighbour(self, i,j, entity):
        if(i>0 ):
            neighbour = self.game_class_array[i-1][j]
            entity.west = neighbour if neighbour!=None else None
        if(j>0): 
            neighbour = self.game_class_array[i][j-1]
            entity.north = neighbour if neighbour!=None else None         
        if(i<(map_height-1)): 
            neighbour = self.game_class_array[i+1][j]
            entity.south = neighbour if neighbour!=None else None           
        if(j<(map_width-1)):
            neighbour = self.game_class_array[i][j+1]
            entity.east = neighbour if neighbour!=None else None
                    
    def build_map(self):
        map_func =  lambda classid: \
                    place_class_dict[classid]() if classid!='##' else None
    
        self.game_class_array = np.array(list(map(map_func, self.entity_list)))\
                                  .reshape((map_height, map_width))

        for (i,j), entity in np.ndenumerate(self.game_class_array):
            if(entity):
                self.game_map.add_entity(entity.__str__, entity)
                self.add_neighbour( i,j, entity)