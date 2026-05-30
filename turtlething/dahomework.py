import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # You can change this to any color (e.g., "pink", "black")

# Create a turtle named 'Dharani'
dharani = turtle.Turtle()
dharani.color("darkblue")
dharani.pensize(3)
dharani.speed(3)

# Draw a square
for i in range(4):
    dharani.forward(100)  # Move forward 100 units
    dharani.left(90)     # Turn left 90 degrees

# Keep the window open
turtle.done()
