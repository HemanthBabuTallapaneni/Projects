import turtle as t
import random
t.colormode(255)
a = t.Turtle()
a.speed("fastest")
a.penup()
a.hideturtle()
color = [(246, 244, 243), (235, 240, 246), (247, 240, 243), (240, 246, 243), (133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]
a.setheading(225)
a.forward(300)
a.setheading(0)
dots = 101
for s in range(1,dots):
    a.dot(20,random.choice(color))
    a.forward(50)
    if s % 10 == 0:
        a.setheading(90)
        a.forward(50)
        a.setheading(180)
        a.forward(500)
        a.setheading(0)
screen = t.Screen()
screen.exitonclick()
