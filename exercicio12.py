import turtle                       #Nod permite usar tartarugas
wn = turtle.Screen()                #Cria o background
wn.bgcolor("lightgreen")            #Colore o background

cep = turtle.Turtle()               #Cria a tartaruga cep
cep.shape("turtle")                 #Seta o formato de Cep
cep.color("blue")                   #Seta a cor de Cep

cep.penup()                         #Faz com que Cep nao crie linhas
size = 150                          #Determina o raio do "relogio"

for i in range(12):                 #Loop para criar o relógio
   cep.forward(size)                #Anda para o local determinado
   cep.stamp()                      #Marca o local com a tartaruga
   cep.left(180)                    #Vira-se para o centro
   cep.forward(size)                #Retorna ao centro
   cep.left(150)                    #Vira-se para o proximo local determinado

wn.mainloop()
