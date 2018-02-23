import turtle                           #Nos permite usar tartarugas
wn = turtle.Screen()                    #Cria o espaço para as tartarugas
wn.bgcolor("lightgreen")                #Seta a cor do background
wn.title("Capitulo 3 - Exercicio 6")    #Nomeia a janela

#Construindo um triângulo equilátero

bittar = turtle.Turtle()                #Cria a primeira tartaruga
bittar.shape("turtle")                  #Seta o formato de bittar
bittar.color("blue")                    #Seta a cor da tartaruga

for i in range(3):                      #Loop para fazer o triângulo equilátero
    bittar.forward(50)
    bittar.left(120)

#Construindo um quadrado

goffi = turtle.Turtle()
goffi.shape("turtle")
goffi.color("Purple")

for i in range(4):
    goffi.forward(50)
    goffi.left(90)

#Construindo um hexagono regular

onze = turtle.Turtle()
onze.shape("turtle")
onze.color("Orange")

for i in range(6):
    onze.forward(50)
    onze.left(60)

#Construindo um octogono regular

garret = turtle.Turtle()
garret.shape("turtle")
garret.color("hotpink")

for i in range(8):
    garret.forward(50)
    garret.left(45)

wn.mainloop()
