from graphics import *
from random import *

def draw_ci (cX, cY, radius, color, win):
    circle = Circle(Point(cX, cY), radius)
    circle.setFill(color)
    circle.draw(win)
    
bullWin = GraphWin("bullsEyes.py", 500, 500)
bullWin.setCoords(0, 0, 500, 500)

def draw_be(bX, bY, rings, rSize, bColor1, bColor2, bWin):
    bSize = rings * rSize
    for i in range (rings):
        if (i) % 2 == 1:
            cCol = bColor1
        else:
            cCol = bColor2
        draw_ci(bX, bY, bSize, cCol, bWin)
        bSize -= rSize

        
draw_be(250, 250, 10, 10, "black", "red", bullWin)

