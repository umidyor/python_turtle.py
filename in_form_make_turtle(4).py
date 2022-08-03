from turtle import *
bgcolor('black')
speed(777)
hideturtle()

for i in range(250):
    color('red')
    circle(i)

    color('orange')
    circle(i*0.8)
    right(3)
    forward(3)
done()