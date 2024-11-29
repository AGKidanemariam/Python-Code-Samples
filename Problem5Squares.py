# Abraham Kidanemariam
# 11/10/24
# Problem 5: Use turtle graphics to draw a square pattern. 

import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(2)

# Function to draw squares
def draw_squares(size):
    """Draws squares in a loop with Turtle graphics."""
    for i in range(4):  # Each square side
        t.forward(size)
        t.right(90)
    t.penup()
    t.forward(size + 10)
    t.pendown()

# Loop to draw multiple squares
for i in range(5):
    draw_squares(50)

turtle.done()
