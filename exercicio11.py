import turtle                           #Nos permite usar tartarugas
wn = turtle.Screen()                    #Cria o espaço para as tartarugas
wn.bgcolor("lightgreen")                #Seta a cor do background
wn.title("Capitulo 3 - Exercicio 6")    #Nomeia a janela

coco = turtle.Turtle()                  #Cria a tartaruga coco
coco.shape("turtle")                    #Seta o formato da tartaruga
coco.color("blue")                      #Seta a cor da tartaruga
coco.pensize(3)                         #Seta a espessura do traço

#Criando uma estrela de cinco pontas

coco.left(36)                           #Coloca a tartaruga na posição inicial

for i in range(5):                      #Faz o loop da estrela
    coco.forward(150)
    coco.left(144)

wn.mainloop()
