
import os
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from level import *
from pacman import *
import time
import pygame


pygame.init()
screen = pygame.display.set_mode((1, 1)) #hack needed to get the keyhandler to function

def main():
    path = "./Levels/level1" #default starting level
    level = Level(path) #Init level with path to config file
    theatre = Theatre(level) #setup theatre || canvas
    theatre.loop() #Init gameloop


class Theatre():

    def __init__(self,level):
        self.level = level
        self.fps = 5.0

    def update(self):

        #aliases
        pX = self.level.pacman.posX
        pY = self.level.pacman.posY

        #movement
        key = self.keyHandler()
        self.level.pacman.movement(key)

        #aliases
        x = self.level.pacman.posX
        y = self.level.pacman.posY
        obj = self.level.scene[y][x]
        pac = self.level.pacman

        #collision handler
        if (pac.collision(obj)):
            for key, value in self.level.actors.items():
                if (isinstance(obj, key)):
                    if (pac.collide(self.level.actors[key])):
                        #swap
                        self.level.scene[pY][pX] = Floor()
                        self.level.scene[y][x] = self.level.pacman
                    obj.collide(self.level.actors[Pacman])

    def keyHandler(self):
        key = ""
        events = pygame.event.get()
        for event in events:
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_LEFT):
                    key = "left"
                if (event.key == pygame.K_RIGHT):
                    key = "right"
                if (event.key == pygame.K_UP):
                    key = "up"
                if (event.key == pygame.K_DOWN):
                    key = "down"
        return key

    def clear(self):
        os.system('clear')

    def render(self):
        self.clear()
        for row in self.level.scene:
            state = ""
            for col in row:
                state += col.render() + " "
            print(state)

    #quick calling function with a timer.
    def loop(self):
        alarm = 1/self.fps
        tStamp = 0
        while True:
            if (tStamp == 0):
                tStamp = time.time()
            if (time.time() - tStamp > alarm):
                self.update()
                self.render()
                tStamp = 0


if __name__ == "__main__":
    main()
