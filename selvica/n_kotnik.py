import turtle



window = turtle.Screen()
zelvica = turtle.Turtle()

# n = int(input("Vnesi stevilo kotov"))
n = 12
notranji_kot = 360/n # 180 * (n-2)/n
# dolzina = int(input("Vnesi dolzino stranice"))
dolzina = 100
                # ff00ff
zelvica.pencolor("#000000")

seznam_barv = ["green", "red", "blue", "orange", "pink", "black", "brown"]


print(seznam_barv[3])


for stranica in range(n):

    zelvica.pencolor(seznam_barv[ stranica % len(seznam_barv)])

    zelvica.forward(dolzina)
    zelvica.right(notranji_kot)

turtle.done()






