import turtle

pen = turtle.Turtle()
turtle.bgcolor("light blue")
pen.pensize(1.5)
pen.color("black", "White")

def goto(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


# Head
goto(0, 150)
pen.circle(50)

# Eyes

goto(22, 205)
pen.begin_fill()
pen.circle(8)
goto(-22, 205)
pen.circle(8)
pen.end_fill()
# Dahan
goto(-22, 180)
pen.forward(50)

# Kolah
pen.color("black", "black")
goto(-65, 235)
pen.begin_fill()
pen.forward(130)
pen.left(90)
pen.forward(30)
pen.left(90)
pen.forward(30)
pen.right(90)
pen.forward(60)
pen.left(90)
pen.forward(70)
pen.left(90)
pen.forward(60)
pen.right(90)
pen.forward(30)
pen.end_fill()

# Body
goto(0, -50)
goto(0, -50)
pen.right(180)
pen.circle(100)

# Legs

goto(0, -350)
pen.circle(150)


# Left arm

goto(100, 65)
pen.left(30)
pen.forward(100)
temp_x = pen.xcor()
temp_y = pen.ycor()
pen.left(30)
pen.forward(30)
goto(temp_x, temp_y)
pen.right(75)
pen.forward(30)


# Right arm

goto(-100, 65)
pen.left(180)
pen.forward(80)
pen.right(45)
pen.forward(65)
temp_x = pen.xcor()
temp_y = pen.ycor()
pen.right(30)
pen.forward(30)
goto(temp_x, temp_y)
pen.left(60)
pen.forward(30)

turtle.done()