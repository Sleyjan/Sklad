from graphics import *

win=GraphWin('oyna',400,400)


obj3 = Rectangle(Point(0, 0), Point(400, 200))

tonka = Rectangle(Point(145, 250), Point(155, 300))

obj2 = Rectangle(Point(0, 200), Point(400, 400))

kolmak= Oval(Point(100,300),Point(200,310))

obj = Polygon(Point(100,200),Point(150,150),Point(200,200))

shape = obj.clone()

shape1 = shape.clone()

shape.move(-0,25)

shape1.move(-0,50)

obj4 = Circle(Point(300,75), 25 )

bulut = Circle(Point(100,75), 25 )
bulut1 = bulut.clone()
bulut2 = bulut.clone()
bulut3 = bulut.clone()
bulut4 = bulut.clone()

bulut1.move(-30,0)
bulut2.move(0,30)
bulut3.move(-30,30)
bulut4.move(-60,30)


obj4.setOutline("black")


kolmak.setOutline("White")

tonka.setOutline("black")

bulut.setOutline("black")

obj2.setOutline("Blue")

obj3.setOutline("blue")

obj.setOutline("black")

obj4.setFill("yellow")

tonka.setFill("brown")

kolmak.setFill("black")

bulut.setFill("white")

bulut1.setFill("white")

bulut2.setFill("white")

bulut3.setFill("white")

bulut4.setFill("white")

obj2.setFill("grey")

obj.setFill("green")

shape.setFill("green")

shape1.setFill("green")

obj3.setFill("blue")


obj2.draw(win)

obj3.draw(win)

obj4.draw(win)

shape1.draw(win)

shape.draw(win)

bulut.draw(win)
bulut1.draw(win)
bulut2.draw(win)
bulut3.draw(win)
bulut4.draw(win)
kolmak.draw(win)
tonka.draw(win)
obj.draw(win)


win.getMouse()


win.close()
