import turtle


def circle(turtle, radius):
    for _ in range(40):
        turtle.circle(radius)
        turtle.right(90)
        radius -= 5

def circles(turtle, radius):
    for color in ["red", "green", "yellow", "blue", "peach puff", "light green"]:
        turtle.color(color)
        circle(Bob, 200)
        turtle.right(90)

Bob = turtle.Turtle()
Bob.speed(0)
window = turtle.Screen()
window.bgcolor("black")

circles(Bob, 200)

window.mainloop()
