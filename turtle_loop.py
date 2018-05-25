import turtle
tess = turtle.Turtle()
tess.pensize(7)
colour=['green','yellow','red','violet','blue']
for i in colour:
    tess.color(i)
    tess.forward(120)
    tess.left(-90)
    tess.forward(120)
    tess.left(-90)
    tess.forward(120)
    tess.left(-90)
    tess.forward(120)
    tess.speed(1)
