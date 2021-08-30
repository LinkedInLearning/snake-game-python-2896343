# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 20  # Milliseconds between screen updates.


def move_turtle():
    my_turtle.forward(1)
    my_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, DELAY)


# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Animation Example")
screen.bgcolor("cyan")
screen.tracer(0)  # Turns off automatic animation

# Create a turtle to do your bidding
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

# Set animation in motion
move_turtle()

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()
