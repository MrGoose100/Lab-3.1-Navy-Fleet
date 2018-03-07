from updatedGraphics import *
win = GraphWin("Navy Fleet",1000,650, autoflush=False)






class Background(object):
    def drawOcean(win):
        ocean = Rectangle(Point(0,450), Point(999,649))
        ocean.setFill("blue")
        ocean.draw(win)

    def drawLand(win):
        land = Rectangle(Point(0,300), Point(300,450))
        land.setFill("brown")
        land.draw(win)


Background.drawOcean(win)
Background.drawLand(win)
win.getMouse()









