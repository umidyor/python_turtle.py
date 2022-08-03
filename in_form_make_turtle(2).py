from turtle import *
bgcolor('red')
speed(100)
hideturtle()

for i in range(500):
    color('black')
    circle(i)

    color('blue')
    circle(i*0.8)
    right(90)
    forward(100)
done()