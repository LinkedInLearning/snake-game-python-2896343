# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500

# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Program Title")
screen.bgcolor("cyan")

# Create a turtle to do your bidding
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

# Your turtle awaits your command
my_turtle.forward(100)  # Sample command

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()
