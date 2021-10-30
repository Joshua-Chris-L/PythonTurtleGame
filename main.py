# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import turtle
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

#Turtle
tim = Turtle(shape="turtle")
shaw = Turtle(shape="turtle")
shun = Turtle(shape="turtle")
gimm = Turtle(shape="turtle")
bann = Turtle(shape="turtle")
bamb = Turtle(shape="turtle")

#color, shape and coordinate of each turtle2
shaw.penup()
shaw.goto(x=-230, y=-70)
shaw.color("red")

#color, shape and coordinate of each turtle1
tim.penup()
tim.goto(x=-230, y=-40)
tim.color("blue")

#color, shape and coordinate of each turtle3
shun.penup()
shun.goto(x=-230, y=-10)
shun.color("green")

#color, shape and coordinate of each turtle4
gimm.penup()
gimm.goto(x=-230, y=20)
gimm.color("orange")

#color, shape and coordinate of each turtle5
bann.penup()
bann.goto(x=-230, y=50)
bann.color("pink")

#color, shape and coordinate of each turtle5
bamb.penup()
bamb.goto(x=-230, y=80)
bamb.color("brown")
#print(user_bet)
import  random

all_turtles = [tim, shaw, shun, gimm, bamb, bann]
is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
