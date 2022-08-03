from turtle import *        #It's turtle library
bgcolor('red')              #This form is for changing background image...
speed(100)                  #This is a command that sets the speed of drawing a shape!
hideturtle()

for i in range(500):
    color('black')          #This is a command that gives the color of the outline of the shape being drawn!
    circle(i)               #This command specifies that the shape will be circular!

    color('blue')           #This is the command that gives the shape's interior color. That is, the second color.
    circle(i*0.8)
    right(90)               #This is a command that specifies how many degrees to rotate the shape to the right. Now it's drawing this shape at 90 degrees!
    forward(100)
done()    #-> And that means closing the program!
