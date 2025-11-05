import turtle

pen = turtle.Turtle()


def goto(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


goto(-250, 0)
for x in range(3):
    goto((x*225)-250, 0)
    pen.circle(100)
goto(-135, -100)
pen.circle(100)
goto(90, -100)
pen.circle(100)

turtle.done()