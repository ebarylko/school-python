#ch3ex1.py
#Eitan

import turtle

def turtle_square(turtle, coordinates):
    forward = 200
    position = tess.forward(coordinates)
    for _ in range(22):
        tess.forward(forward)
        tess.left(90)
        forward -= 10


window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.left(180)

turtle_square(tess, 200)

window.mainloop()
