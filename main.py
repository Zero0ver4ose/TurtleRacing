from turtle import Turtle, Screen
import random

game_is_on = True
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "pink"]
y_position = [-100, -50, 0, 50, 100]
all_turtles = []


for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(x=-240, y=y_position[turtle_index])
    all_turtles.append(new_turtle)


while game_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 250:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                game_is_on = False

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()