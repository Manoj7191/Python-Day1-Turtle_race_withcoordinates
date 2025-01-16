from turtle import Turtle, Screen
import random

is_race_on = False
scr=Screen()
scr.setup(width=500,height=400)
user_guess=scr.textinput(title="Make a bet",prompt="Which turtle will win the race? Enter the color:")
colors = [ "red","green","yellow","blue","orange","black"]
print(user_guess)
xaxis = -230
yaxis = -80
turtles = []

if user_guess:
   is_race_on = True
else:
   exit("No user bet Hence abending the race")

for _ in colors:
   new_turtle = Turtle(shape="turtle")
   new_turtle.color(_)
   new_turtle.penup()
   new_turtle.goto(xaxis,yaxis)
   yaxis += 30
   turtles.append(new_turtle)

while is_race_on:
   for tur in turtles:
      random_distance = random.randint(0,10)
      tur.forward(random_distance)
      print(tur.xcor())
      if tur.xcor() >= 230:
         is_race_on = False
         if tur.pencolor() == user_guess:
            print(f"YOU WIN as the guess {tur.pencolor()} has won the race ")
            break
         else:
            print(f"YOU LOOSE as {tur.pencolor()} has won the race")
            break

scr.exitonclick()