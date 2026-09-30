
def set(x:float, y:float):
    t.pu()
    t.setpos(x, y)
    t.pd()

def elips(x:float):
    for i in range(2):
        turtle.circle(x, 90)
        turtle.circle(x//2, 90)

def star():
    set(random.uniform(-400,400), random.uniform(-350,350))
    t.color('white')
    t.fillcolor('white')
    t.begin_fill()
    t.circle(2)
    t.end_fill()

def big_star():
    set(random.uniform(-400,400), random.uniform(-350,350))
    t.color('white')
    t.fillcolor('white')
    t.begin_fill()
    for i in range(4):
        t.circle(7,90)
        t.right(180)
    t.end_fill()
    
def drawing():
        #sun
    t.color('#CE590B')
    t.pensize(3)
    t.begin_fill()
    t.fillcolor('yellow')
    set(0, -50)
    t.circle(55)
    t.end_fill()

    t.pensize(2)
    set(5, -40)
    t.circle(35, 90)

    set(10, -33)
    t.setheading(0)
    t.circle(20, 45)

    set(-8, 40)
    t.left(140)
    t.circle(35, 90)

    set(-15, -50)
    t.pensize(3)
    t.setheading(270)

    for i in range(12):
        t.circle(50, 45)
        t.left(90)
        t.circle(50, 45)
        t.right(150)

    #jupiter
    t.pensize(5)
    set(-217.0, -112.0)
    t.color('brown')

    t.fillcolor('orange')
    t.begin_fill()
    t.circle(45)
    t.end_fill()

    t.lt(120)
    t.circle(80, 40)


    set(-165.0, -68.0)
    t.lt(160)
    t.circle(100, 50)

    set(-159.0, -112.0)
    t.seth(200)
    t.fillcolor('red')
    t.begin_fill()
    elips(10)
    t.end_fill()

    set(-149.0, -148.0)
    t.seth(60)
    t.circle(150, 20)

    #saturn
    t.pensize(3)

    t.color('#8D7B25')
    t.fillcolor('#D0B637')
    t.begin_fill()
    set(230.0, 103.0)
    t.circle(45)
    t.end_fill()

    t.color('#766409')
    set(141.0, 123.0)
    t.seth(180)
    t.pensize(5)
    t.circle(100, 10)
    t.seth(330)
    t.circle(200, 37)
    t.seth(145)
    t.circle(100, 10)

    #Earth 
    t.pensize(3)
    t.color('#290AA6')
    t.fillcolor('blue')
    t.begin_fill()
    set(217.0, -84.0)
    t.circle(40)
    t.end_fill()

    #orbit of the earth
    set(228.0, -63.0)
    t.color('white')
    t.pensize(1)
    for i in range(20):
        t.pd()
        t.circle(65, 9)
        t.pu()
        t.circle(65, 9)
    t.pd()

    #moon
    t.pensize(2)
    t.color('gray')
    t.fillcolor('white')
    t.begin_fill()
    t.right(90)
    t.circle(10)
    t.end_fill()

    set(218.0, -57.0)
    t.pensize(3)
    t.color('gray')
    t.circle(2)

    #green part of the earth 
    set(188.0, -83.0)
    t.color('green')
    t.fillcolor('green')
    t.seth(290)
    t.begin_fill()
    t.circle(-10, 90)
    t.circle(10, 90)
    t.right(90)
    t.circle(-40, 20)
    t.right(103)
    t.circle(-40, 60)
    t.end_fill()

    set(181.0, -122.0)
    t.begin_fill()
    t.circle(-10, 90)
    t.left(50)
    t.circle(-10,90)
    t.forward(10)
    t.right(90)
    t.circle(-10, 50)
    t.left(10)
    t.circle(-20, 30)
    t.left(90)
    t.circle(-10, 120)
    t.end_fill()

    set(238.0, -128.0)
    t.begin_fill()
    t.left(27)
    t.circle(50, 50)
    t.left(75)
    t.circle(20,40)
    t.right(90)
    t.circle(10, 60)
    t.circle(50, 10)
    t.left(90)
    t.circle(20, 60)
    t.right(90)
    t.circle(50, 20)
    t.left(50)
    t.circle(-10, 60)
    t.end_fill()

    #drawing a comet

    #star
    set(-78.0, 204.0)
    t.color('yellow')
    t.fillcolor('yellow')
    t.begin_fill()
    size = 30
    for i in range(3):
        t.fd(size)
        t.lt(120)
    set(-63.0, 212.0)
    t.end_fill()
    t.begin_fill()
    for i in range(3):
        t.fd(size)
        t.right(120)
    t.end_fill()

    #tail of the comet 
    t.pensize(2)
    t.pencolor('orange')
    set(-79.0, 200.0)
    t.seth(165)
    t.circle(150, 50)   
    t.goto(-161.0, 186.0)   

    set(-80.0, 188.0)
    t.seth(197)
    t.circle(150, 45)
    t.goto(-156.0, 156.0)

    set(-78.5, 194.0)
    t.seth(180)
    t.circle(150, 40)
    t.goto(-164.0, 185.0)

    set(-77.0, 196.0)
    t.seth(170)
    t.circle(150, 33)

    set(-79.0, 191.0)
    t.seth(187)
    t.circle(150, 33)
    t.goto(-177.0, 160.0)

    #planet
    t.color('gray')
    t.fillcolor('lightblue')
    t.pensize(3)
    set(-276.0, 76.0)
    t.begin_fill()
    t.circle(40)
    t.end_fill()

    t.fillcolor('gray')
    set(-241.0, 24.0)
    t.seth(180)
    t.begin_fill()
    elips(5)
    t.end_fill()

    set(-224.0, 43.0)
    t.begin_fill()
    elips(7)
    t.end_fill()

    set(-245.0, 48.0)
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    set(-257.0, 73.0)
    t.left(15)
    t.circle(30, 90)

    #thing that orbits 
    set(-39.0, -146.0)
    t.color('white')
    t.pensize(1)
    t.seth(280)
    for i in range(5):
        t.pd()
        t.circle(80, 9)
        t.pu()
        t.circle(80, 9)
    t.pd()
    t.pensize(2)
    set(90.0, -211.0)
    t.fillcolor('gray')
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    set(54.0, -211.0)
    t.circle(200, 10)

    set(91.0, -211.0)
    t.right(170)
    t.circle(-80, 30)
    set(85.0, -192.0)
    t.seth(180)
    t.circle(80, 30)

    #roket
    set(126.0, 206.0)
    t.color('gray')
    t.fillcolor('lightgrey')
    t.begin_fill()
    t.seth(180)
    t.circle(-85, 50)
    t.right(100)
    t.circle(-85, 50)
    t.right(80)
    t.fd(35)
    t.end_fill()

    set(131.0, 236.0)
    t.right(90)
    t.fd(50)

    set(127.0, 212.0)
    t.fd(50)
    t.update()

    set(99.0, 238.0)
    t.color('black')
    t.fillcolor('black')
    t.begin_fill()
    t.circle(8.5)
    t.end_fill()

    t.color('orange')
    t.fillcolor('orange')
    t.begin_fill()
    set(129.0, 224.0)
    t.right(145)
    t.circle(-30, 70)
    t.right(110)
    t.circle(-30, 70)
    t.end_fill()


def get_mouse_click_coor(x,y):
   print(f'({x}, {y})')

def astronaut(x: float, y:float):
    set(x, y)
    size = 5
    #head
    t.color('gray')
    t.fillcolor('lightgray')
    t.seth(0)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    t.pu()
    t.left(90)
    t.fd(size/3)
    t.right(90)
    t.pd()
    t.color('black')
    t.fillcolor('black')
    t.begin_fill()
    t.circle(size/1.8)
    t.end_fill()

    #body

    t.color('gray')
    t.fillcolor('lightgray')
    t.pu()
    t.right(90)
    t.fd(3)
    t.left(90)
    t.fd(size/2)
    t.pd()

    t.begin_fill()
    t.circle(size, 80)
    t.right(80)
    t.circle(-size/2, 60)
    t.right(35)
    t.circle(-size, 80)
    t.left(90)
    t.forward(size*2)

    t.circle(-size/2, 180)
    t.right(5)
    t.forward(size/2.5)
    t.circle(size/5, 180)
    t.forward(size/2.5)
    t.circle(-size/2, 180)
    t.right(5)
    t.fd(size*2)

    t.left(80)
    t.circle(-size, 80)
    t.right(25)
    t.circle(-size/2, 60)
    t.right(90)
    t.circle(size, 80)
    t.end_fill()
    t.fd(size/5)

    t.pu()
    t.seth(270)
    t.fd(size/2)
    t.right(90)
    t.fd(size/4)
    t.left(90)
    t.pd()
    t.fillcolor('black')
    t.begin_fill()
    for i in range(2):
        t.fd(size/1.3)
        t.left(90)
        t.fd(size*1.17)
        t.left(90)
    t.end_fill()



import turtle
import random
t = turtle
screen = t.Screen()
t.tracer(0, 0)
t.hideturtle()
screen.bgcolor('#1B1212')

for i in range(50):
    big_star()

for i in range(250):
    star()

drawing()

t.onscreenclick(get_mouse_click_coor)

t.onscreenclick(astronaut)

t.update()
t.done()