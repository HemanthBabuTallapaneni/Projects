from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
a = screen.textinput(title="Make your bet",prompt="Which turtle will win thw race? Enter a color:")
colors = ["red","blue","green","yellow","orange","purple"]
y = [-60,-30,0,30,60,90]
all_turtles = []
for i in range(0,6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-230,y[i])
    all_turtles.append(t)
if a:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == a:
                print(f"You win! The {winner} turtle wins.")
            else:
                print(f"You lose! The {winner} turtle wins.")
                is_race_on = False
        distance = random.randint(0,10)
        turtle.forward(distance)
screen.exitonclick()
