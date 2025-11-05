import turtle

pen = turtle.Turtle()
pen.pensize(1.5)

def goto(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


pen.dot(10)
goto(100, 100)
pen.dot(10)
pen.goto(-100, -100)
pen.dot(10)
goto(-100, 100)
pen.dot(10)
pen.goto(100, -100)
pen.dot(10)
pen.goto(100,100)
goto(-100,100)
pen.goto(-100,-100)

def khat():
    x = 43
    y = 28
    z = 20
    for i in range(3):
        pen.forward(y if i == 0 else x)
        goto(pen.xcor() + z, pen.ycor())
    pen.forward(y)
khat()
goto(-100,100)
khat()
turtle.done()
