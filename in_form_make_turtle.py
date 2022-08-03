from turtle import *

bgcolor('black')
speed(100)
hideturtle()

for i in range(500):
    color('red')
    circle(i)

    color('blue')
    circle(i*0.8)
    right(56)
    forward(3)
done()