from graphics import *
from random import *

bullWin = GraphWin("bullsEyes.py", 500, 500)
bullWin.setCoords(0, 0, 500, 500)

circle = Circle(Point(250, 250), 30)
circle.setFill("green")
circle.draw(bullWin)

