# adapted from https://gist.github.com/zetabeta/5875316
def setup():
    background(255)
    size(400, 400)
    order = 3
    drawSnowFlakeWithOrder(order)

def draw():
    return

def mousePressed(): 
    background(255) 
    order = int(map(mouseY, 0, width, 0, 7))
    drawSnowFlakeWithOrder(order) 

def drawSnowFlakeWithOrder(order):
    side = int(min(width, height) * 0.8)
    triangleHeight = int(side * sin(radians(60.0)))
    p1 = Point(width / 2, 10) 
    p2 = Point(width / 2 - side / 2, 10 + triangleHeight) 
    p3 = Point(width / 2 + side / 2, 10 + triangleHeight) 
    
    r = int(map(order, 0, 7, 0, 255)) 
    g = int(map(mouseX, 0, width, 0, 255)) 
    b = int(map(mouseY, 0, height, 0, 255))
    
    drawSnowFlake(order, p1, p2, 1, r, g, b) 
    drawSnowFlake(order, p2, p3, 1, r, g, b) 
    drawSnowFlake(order, p3, p1, 1, r, g, b) 


class Point():
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
 
    def Point(self, xp, yp):
        self.xp = x 
        self.yp = y
   
    def draw(weight, r, g, b):
        strokeWeight(weight) 
        stroke(r, g, b) 
        point(x,y) 

def drawSnowFlake(order, p1, p2, weight, r, g, b):
    if order == 0: 
        strokeWeight(weight) 
        stroke(r,g,b) 
        line(p1.x, p1.y, p2.x, p2.y) 
    else:
        deltaX = p2.x - p1.x 
        deltaY = p2.y - p1.y 
        cosConst = cos(radians(30.0)) 
        zx = int((p1.x + p2.x)/2 + cosConst * (p1.y - p2.y)/3.0)
        zy = int((p1.y + p2.y)/2 + cosConst * (p2.x - p1.x)/3.0)
        x = Point(p1.x + deltaX / 3, p1.y + deltaY / 3) 
        y = Point(p1.x + deltaX * 2 / 3, p1.y + deltaY * 2 / 3) 
        z = Point(zx, zy) 
    
        drawSnowFlake(order - 1, p1, x, 1 , r, g, b) 
        drawSnowFlake(order - 1, x, z, 1 , r, g, b) 
        drawSnowFlake(order - 1, z, y, 1 , r, g, b) 
        drawSnowFlake(order - 1, y, p2, 1 , r, g, b)
