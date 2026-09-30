def triangle():
    turtle.forward(30)
    turtle.right(120)
    turtle.forward(30)
    turtle.left(120)
def reset():
    turtle.forward(30)
    turtle.left(120)
    turtle.forward(300)

import turtle
turtle.tracer(0)    
turtle.hideturtle()
turtle.color('blue')

turtle.penup()
turtle.setposition(-100, 100)
turtle.pendown()


turtle.forward(300)
turtle.right(120)
for i in range(0,5):
    for i in range(0,10):
        triangle()

    reset()
    turtle.right(120)

    for i in range(0,10):
        triangle()

    reset()
    turtle.forward(30)
    turtle.right(120)

turtle.color('white')
turtle.right(60)
turtle.forward(29)

turtle.update()       
turtle.done()         
