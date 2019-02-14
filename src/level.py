
from pacman import Pacman

class Dot:
    
    def __init__(self):
        self.sprite = "."
        self.consumed = False

    #Use if requires response
    def collide(self, obj):
        if (obj == "pacman"):
            self.consumed = True
    
    def render(self):
        return self.sprite

class Wall:

    def __init__(self):
        self.sprite = "="

    #Use if requires response
    def collide(self, obj):
        pass
    
    def render(self):
        return self.sprite
       
class Floor:

    def __init__(self):
        self.sprite = " "

    #Use if requires response
    def collide(self, obj):
        pass


    def render(self):
        return self.sprite

class Level:

    def __init__(self, path):
        self.scene = []
        self.path = path
        self.pacman = None
        self.actors = {Dot : "dot", Wall : "wall", Floor : "floor", Pacman : "pacman"}
        self.loadLevel()
    
    def changeLevel(self, path): #not used :: not tested
        self.path = path
        self.loadLevel()

    def prologue(self, f):
        line = "" 
        while (line != "START"):
            line = f.readline()
            line = line[:-1] #get rid of newline char
   
    def populate(self, f):
        posY = 0
        for line in f:
            line = line[:-1] #trash new line
            temp = []
            posX = 0
            #parse
            for char in line:
                if (char == "0"):
                    temp.append(Dot())
                elif (char == "1"):
                    self.pacman = Pacman(posX,posY)
                    temp.append(self.pacman)
                elif (char == "2"):
                    temp.append(Wall())
                posX += 1
            posY += 1
            #append
            if (len(temp) > 0):
                self.scene.append(temp)

    def loadLevel(self):
        f = open(self.path, 'r')
        self.prologue(f)
        self.populate(f)
        f.close()
