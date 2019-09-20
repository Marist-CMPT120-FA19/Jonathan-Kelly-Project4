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
    
    #pauses program for 1 second 
    time.sleep(1)
    
    light.setFill("yellow")
    light.move(0,45)
    
    time.sleep(1)
    
    light.setFill("green")
    light.move(0,45)
    
    time.sleep(2)
        
    win.close()
main()