

class Pacman:

    def __init__(self,x,y):
        self.sprites = {"up" : "v", "right" : "<", "down" : "^", "left" : ">" }
        self.sprite = self.sprites["up"]
        self.currOrientation = "up"
        self.posX = x
        self.posY = y
        self.prevX = None #previous position
        self.prevY = None
 
    def collision(self, obj):
        collide = False
        if (obj != "pacman"):
            collide = True
        return collide

    def collide(self, obj):
        move = False
        if (obj == "wall"):
            self.posY = self.prevY
            self.posX = self.prevX
        else:
            move = True
        return move
  
    def movement(self, moveKey):
        self.prevY = self.posY
        self.prevX = self.posX
        if (self.currOrientation == moveKey): #if he is facing current direction :: move
            if (moveKey == "down"):
                self.posY += 1
            elif (moveKey == "up"):
                self.posY -= 1
            elif (moveKey == "left"):
                self.posX -= 1
            elif (moveKey == "right"):
                self.posX += 1
        else: #change rotation
            if (moveKey != ''):
                self.currOrientation = moveKey
                self.sprite = self.sprites[moveKey]
    
    def render(self):
        return self.sprite
        
