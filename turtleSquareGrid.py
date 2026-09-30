def right():
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(225)

def left():
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(225)

import turtle
turtle.tracer(0)      
turtle.hideturtle()
turtle.color('blue')

turtle.penup()
turtle.setposition(-100, 100)

turtle.pendown()
turtle.forward(225)

for i in range(1,8):
    right()
    left()
right()

turtle.right(90)
turtle.forward(225)

for i in range(1,8):
    right()
    left()
right()

turtle.update()      
turtle.done()   