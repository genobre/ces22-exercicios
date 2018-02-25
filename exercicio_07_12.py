import turtle                   #Nos permite usar a biblioteca turtle
import math                     #Nos permite usar a biblioteca math

def draw_line (t,f,a):
    """Função que faz com que a tartaruga t vira um ângulo a para a
    esquerda e ande f"""
    t.left(a)
    t.forward(f)

#Iniciando o ambiente da tartaruga
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Capítulo 07 - Exercício 12")

#Criando a tartaruga alex
alex = turtle.Turtle()
alex.pensize(4)
alex.color("green")
alex.hideturtle()

#Define os tamanhos do quadrado e da diagonal
l = 100
d = l*math.sqrt(2)

#Lista de duplas de ângulo e tamanhos
moves = [(0,l),(90,l),(90,l),(90,l),(135,d),(75,l),(120,l),(75,d)]

#Loop que lê todos os parâmetros da lista e desenha com eles
for (angle,size) in moves:
    draw_line(alex,size,angle)

wn.mainloop()
