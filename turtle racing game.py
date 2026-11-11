
import turtle
import time
import random

WIDTH,HEIGHT = 500, 500

colors = ["red", "green", "blue", "yellow", "magenta"]

random.shuffle(colors)

def turtle_userinput():
    while True:
        enter=input("Enter the number of turtles(2-5): ")

        if  enter.isdigit():
            enter = int(enter)
            if enter < 2 or enter > 5:
                print("Enter a number between 2 and 5")
            else:
                return enter
        else:
            print("Enter a number between 2 and 5")

def turtle_racer():
    turtle.Screen()
    turtle.bgcolor("white")
    turtle.title("Turtle Racer")

def turtle_draw(t):
    t.shapesize(2)
    t.shape("turtle")
    t.penup()
    t.setpos(WIDTH / 2 - i*150 , -HEIGHT / 2 + 10)
    t.pendown()
    t.left(90)
    t.color(colors[i])

def turtle_race(t):
    t.shape("turtle")
    t.speed(1)
    t.forward(45*(random.randint(1,10)))

racer=[]
number=turtle_userinput()

turtle_racer()

for i in range(number):
    t = turtle.Turtle()
    turtle_draw(t)
    racer.append(t)
for t in racer:
    turtle_race(t)

winner = racer[0]

for t in racer:
    if t.ycor() > winner.ycor():
        winner = t

winner = winner.pencolor()

print("The winner is the turtle with color:", winner)
time.sleep(5)