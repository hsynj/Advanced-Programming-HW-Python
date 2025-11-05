import turtle

pen = turtle.Turtle()
pen.pensize(2)

def goto(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

pen.circle(50)

goto(210, 40)
pen.write("East", font=("Arial", 18, "normal"))
goto(200,50)
pen.backward(400)
goto(-260,40)
pen.write("West", font=("Arial", 18, "normal"))

goto(-23,255)
pen.write("North", font=("Arial", 18, "normal"))
goto(0,250)
pen.right(90)
pen.forward(400)
goto(-23, -180)
pen.write("South", font=("Arial", 18, "normal"))

turtle.done()
