import turtle

pen = turtle.Turtle()

def goto(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def square():
    for x in range(4):
        pen.forward(100)
        pen.right(90)


pen.right(90)
square()
goto(100,-100)
square()
goto(-100,-100)
pen.goto(0,-200)
goto(100,-100)
pen.goto(0,0)
goto(-100,0)
pen.goto(100,-200)
turtle.done()