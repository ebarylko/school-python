import turtle

def circle(turtle, radius):
    for _ in range(40):
        turtle.circle(radius)
        radius -= 5

def circles(turtle, radius):
    for color in ["red", "green", "yellow", "blue"]:
        turtle.color(color)
        circle(Bob, 200)
        turtle.right(90)

window = turtle.Screen()
window.bgcolor("black")
Bob = turtle.Turtle()
Bob.color("peach puff")
Bob.speed(0)
circles(Bob, 200)

window.mainloop()

