import turtle           #Importa a biblioteca que nos permite usar turtle

#Função para desenhar estrela de 5 pontas, recebe como parâmetro uma tartaruga
def make_star(t):
    """Função que desenha estrela regular de 5 pontas, com o tamanho de cada lado
    igual a 100. Recebe como parâmetro tartaruga t"""
    t.hideturtle()
    size = 100                  #Define o lado da estrela como 100
    for i in range(5):          #Loop para fazer a estrela
        t.forward(size)
        t.right(144)

wn = turtle.Screen()                    #Cria e define características da janela
wn.bgcolor("lightgreen")
wn.title("Capítulo 4 - Exercício 9")

alex = turtle.Turtle()                   #Cria e define características da tartaruga
alex.pensize(4)

make_star(alex)                         #Chama função para criar estrela

wn.mainloop()           #Deixa a janela aberta
