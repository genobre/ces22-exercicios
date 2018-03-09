import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Capítulo 10 - Exercício 2")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def draw_housing():
    """ Desenha o sinal de transito """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
tess.forward(40)
tess.left(90)
tess.forward(50)
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

def orange_light():
    tess.forward(70)
    tess.fillcolor("orange")
    wn.ontimer(red_light,1000)

def red_light():
    tess.forward(70)
    tess.fillcolor("red")
    wn.ontimer(green_light,1000)

def green_light():
    tess.back(140)
    tess.fillcolor("green")
    wn.ontimer(orange_light,1000)

orange_light()

wn.listen()                      # Listen for events
wn.mainloop()