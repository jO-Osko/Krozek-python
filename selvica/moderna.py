import random
import turtle
dolz = 100
window = turtle.Screen()
zelvica = turtle.Turtle()

seznam_barv = ["green", "red", "blue", "orange", "pink", "black", "brown"]








random.unfirom(a, b)





zelvica.penup()
for j in range(20):

    dst = dolz

    zelvica.forward(dst)
    zelvica.fillcolor(seznam_barv[ random.randrange(0,7) ])
    zelvica.begin_fill()
    zelvica.circle(3*dst)
    zelvica.end_fill()

    zelvica.right(random.randrange(0, 360))


    dolz = dolz / 1.3


turtle.done()


