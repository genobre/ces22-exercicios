import turtle                       #Nod permite usar tartarugas
wn = turtle.Screen()                #Cria o background
wn.bgcolor("lightgreen")            #Colore o background
wn.title("Capítulo 3 - Exercício 12")        #Define o nome da janela aberta

cep = turtle.Turtle()               #Cria a tartaruga cep
cep.shape("turtle")                 #Seta o formato de Cep
cep.color("blue")                   #Seta a cor de Cep
cep.pensize(3)                      #Seta a espessura da linha

size = 150                          #Determina o raio do "relogio"
space = 10                          #Determina o tamanho da linha que será escrita

cep.penup()                         #Inicia o movimento sem desenhar uma linha

for i in range(12):                 #Loop para criar o relógio
   cep.forward(size)                #Anda para o local determinado
   cep.pendown()                    #Inicia o desenho da linha
   cep.forward(space)               #Desenha a linha
   cep.penup()                      #Termina o desenho da linha
   cep.forward(2*space)             #Anda coma  tartaruga
   cep.stamp()                      #Marca o local com a tartaruga
   cep.left(180)                    #Vira-se para o centro
   cep.forward(size+3*space)        #Retorna ao centro
   cep.left(150)                    #Vira-se para o proximo local determinado

wn.mainloop()
