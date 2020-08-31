import random
import pygame 
import json 
from event_queue import EventQueue
from events import *

FPS = 60 

GRID_WIDTH = 10
GRID_HEIGHT = 20

SCREEN_WIDTH = 470
SCREEN_HEIGHT = 580

INFO_AREA_HEIGHT = 40
INFO_AREA_WIDTH = 200

GAME_WINDOW_WIDTH = SCREEN_WIDTH-INFO_AREA_WIDTH
GAME_WINDOW_HEIGHT = SCREEN_HEIGHT-INFO_AREA_HEIGHT

TILE_WIDTH = int(GAME_WINDOW_WIDTH/GRID_WIDTH)
TILE_HEIGHT = int(GAME_WINDOW_HEIGHT/GRID_HEIGHT)

LEFT_BOUDNARY = 0
RIGHT_BOUNDARY = 1

COLORS = {
    'T' : (100, 65, 175),
    'O' : (255, 213, 0),
    'I' : (3, 65, 174),
    'S' : (114, 203, 59),
    'Z' : (255, 50, 19),
}

event_queue = EventQueue()
clock = pygame.time.Clock()
grid = [[0] * GRID_WIDTH for n in range(GRID_HEIGHT)]
score = 0

with open("shapes.json") as f:
    shapes = json.load(f)

class Bag:
    def __init__(self):
        self.bag_inventory = list(shapes)
        self.bag = self.bag_inventory.copy()
        self.index = 0

    def pop_bag(self):
        return self.bag.pop()

    def reset_bag(self):
        random.shuffle(self.bag_inventory)
        self.bag = self.bag_inventory.copy()

    def next(self):
        if(len(self.bag)) == 0:
            self.reset_bag()
        
        return self.bag[-1]

bag = Bag()
bindings = {
        'escape' : 'QUIT',
        'w' : 'ROTATE',
        "a" : 'MOVE_LEFT',
        'd' : "MOVE_RIGHT",
        's' : 'MOVE_DOWN'
    }

events_map = {
    'QUIT' : QuitGameEvent(),
    'ROTATE' : RotatePieceEvent(),
    'MOVE_DOWN' : MovePieceDownEvent(),
    'MOVE_LEFT' : MovePieceLeftEvent(),
    'MOVE_RIGHT' : MovePieceRightEvent()
}