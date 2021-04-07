# Beginning to draw using the package called turtle

# First step is to import turtle
import turtle

# Make a set-up in turtle

turtle.bgcolor("black")       # giving a background colour
turtle.pensize(2)             # pen size
turtle.color("purple")
turtle.speed(12)

# Draw a square

# turtle.forward(50)            # Moves forward
# turtle.left(90)               # Moves left 90 degrees
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.done()                 # Allows turtle to stay on screen

# A little project using the turtle

# for colours in ["red", "green", "blue", "yellow", "orange", "purple"]:
#     turtle.color(colours)
#     turtle.circle(200)
#     turtle.left(60)
# turtle.done()

# Loop it more to create a better design

for i in range(20):
    for colours in ["violet", "blue", "green", "yellow", "orange", "red"]:
        turtle.color(colours)
        turtle.circle(170)
        turtle.left(3)
turtle.done()



