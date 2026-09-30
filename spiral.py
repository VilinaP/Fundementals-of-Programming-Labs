import turtle

forward = 4
turn = 60
for i in range(500):
    turtle.forward(forward)
    turtle.left(turn)
    turn /= 1.04
    forward += 0.5