from graphics import *
from random import *

def draw_ci (cX, cY, radius, color, win):
    circle = Circle(Point(cX, cY), radius)
    circle.setFill(color)
    circle.draw(win)
    
bullWin = GraphWin("bullsEyes.py", 500, 500)
bullWin.setCoords(0, 0, 500, 500)

draw_ci (250, 250, 50, "black", bullWin)

