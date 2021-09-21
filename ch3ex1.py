#ch3ex1.py
#Eitan

import turtle

def turtle_square(turtle, x, y):
    forward = 200
    turtle.penup()
    turtle.left(180)
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(22):
        turtle.forward(forward)
        turtle.left(90)
        forward -= 10


window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

colors = ["blue", "peach puff", "pink", "gold", "maroon"]


turtle_square(tess, 100, 200)

window.mainloop()
