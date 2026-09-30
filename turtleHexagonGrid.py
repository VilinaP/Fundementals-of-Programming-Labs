def hexagon():
    for i in range (0, 8):
        turtle.forward(15)
        turtle.right(60)
      
def reset():
    turtle.right(120)
    turtle.forward(15)
    turtle.right(60)
    turtle.forward(15)
    turtle.right(30)
    turtle.penup()
    turtle.forward(234)
import turtle   

turtle.tracer(0)     
turtle.color('blue')

turtle.penup()
turtle.setposition(-100, 100)
turtle.pendown()


turtle.left(30)
for i in range(0,5):
    for i in range(0,10):
        hexagon()
        turtle.left(120)

    reset()
    turtle.pendown()
    turtle.right(150)

    for i in range(0,10):
        hexagon()
        turtle.left(120)

    reset()
    turtle.forward(25)
    turtle.right(150)
    turtle.pendown()



turtle.update()       
turtle.done()         