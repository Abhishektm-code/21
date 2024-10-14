import turtle

def draw_stick_figure():
    # Create a turtle object
    pen = turtle.Turtle()
    
    # Draw the head (a circle)
    pen.penup()
    pen.goto(0, 0)  # Start at the center
    pen.pendown()
    pen.circle(20)  # Radius of the head
    
    # Draw the body (a line)
    pen.penup()
    pen.goto(0, -20)  # Move to the bottom of the head
    pen.pendown()
    pen.goto(0, -100)  # Draw the body
    
    # Draw the arms (two lines)
    pen.goto(-30, -60)  # Left arm
    pen.goto(0, -100)   # Back to the body
    pen.goto(30, -60)   # Right arm
    pen.goto(0, -100)   # Back to the body
    
    # Draw the legs (two lines)
    pen.goto(-30, -150)  # Left leg
    pen.goto(0, -100)    # Back to the body
    pen.goto(30, -150)   # Right leg

    # Hide the turtle pointer
    pen.hideturtle()

# Set up the screen
turtle.Screen().bgcolor("white")  # Set background color
draw_stick_figure()

# Finish the drawing
turtle.done()
