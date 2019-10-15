# Jonathan Kelly, 9/19/19, jonathan.kelly2@marist.edu
# creates a stop light that goes from red to yellow to green then closes 

from graphics import *

def main():
    win = GraphWin()
    
    box = Rectangle(Point(100, 170), Point(20, 20))
    box.setOutline("black")
    box.setFill("white")
    box.draw(win)
    
    light = Circle(Point(59,50), 20)
    light.setFill("red")
    light.draw(win)
    
    light = Circle(Point(59,95), 20)
    light.setFill("yellow")
    light.draw(win)
    
    light = Circle(Point(59,140), 20)
    light.setFill("green")
    light.draw(win)
    
        
    win.getMouse()
main()