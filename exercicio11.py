import turtle                           #Nos permite usar tartarugas
wn = turtle.Screen()                    #Cria o espaço para as tartarugas
wn.bgcolor("lightgreen")                #Seta a cor do background
wn.title("Capitulo 3 - Exercicio 11")    #Nomeia a janela

coco = turtle.Turtle()                  #Cria a tartaruga coco
coco.shape("turtle")                    #Seta o formato da tartaruga
coco.color("blue")                      #Seta a cor da tartaruga
coco.pensize(3)                         #Seta a espessura do traço
coco.hideturtle()                       #Esconde a tartaruga

#Criando uma estrela de cinco pontas

for i in range(5):                      #Faz o loop da estrela
    coco.forward(150)
    coco.right(144)

wn.mainloop()
