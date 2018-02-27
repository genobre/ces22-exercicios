#Usamos a seguinte lógica para saber se uma figura é um caminho euleriano
#Se um vértice da figura tiver um número ímpar de caminhos passando por ele, devemos começar
#ou terminar o caminho por ele. Sendo assim, devemos ter apenas dois vértices com um número
#ímpar de caminhos e será por um desses vértices que devemos começar

#Isso acontece com as Figuras 1, 2, 5 e 6

#O código abaixo irá mostrar as quatro figuras sendo feitas dessa maneira

import turtle                   #Nos permite usar a biblioteca turtle
import math                     #Nos permite usar a biblioteca math

def draw_line (t,f,a):
    """Função que faz com que a tartaruga t vira um ângulo a para a
    esquerda e ande f"""
    t.left(a)
    t.forward(f)

def create_turtle(x,y,clr):
    """Função que cria uma tartaruga com a cor escolhida e a coloca na posição inicial"""
    ex = turtle.Turtle()
    ex.hideturtle()
    ex.pensize(4)
    ex.color(clr)
    ex.penup()
    ex.goto(x,y)
    ex.pendown()
    return ex

#Iniciando o ambiente da tartaruga
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Capítulo 07 - Exercício 13")

#Criando as tartarugas
onze = create_turtle(-150,-100,"orange")
bittar = create_turtle(50,-50,"blue")
goffi = create_turtle(50,50,"hotpink")
garret = create_turtle(-100,100,"green")

#Definindo os tamanhos padrões
l = 50
d = l*math.sqrt(2)

#Criando as listas de movimento
figura1 = [(270,l),(90,l),(90,l),(30,l),(120,l),(120,l)]
figura2 = [(180,l),(270,l),(225,d),(135,l),(30,l),(120,l),(120,l)]
figura5 = [(90,l),(120,l),(120,l),(30,l),(30,l),(120,l),(330,l),(120,l),(120,l),(270,l)]
figura6 = [(270,l),(240,l),(240,l),(30,l),(240,l),(30,l),(240,l),(240,l),(135,d),(135,l),(135,d),(225,l)]

#Criando as Figuras
for (angle,size) in figura1:
    draw_line(garret,size,angle)
for (angle,size) in figura2:
    draw_line(goffi,size,angle)
for (angle,size) in figura5:
    draw_line(onze,size,angle)
for (angle,size) in figura6:
    draw_line(bittar,size,angle)

wn.mainloop()
