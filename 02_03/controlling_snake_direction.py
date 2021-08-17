# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 400  # Milliseconds


def move_snake():
    stamper.clearstamps()  # Remove existing stamps made by stamper.

    new_head = snake[-1].copy()
    new_head[0] += 20

    # Add new head to snake body.
    snake.append(new_head)

    # Remove last segment of snake.
    snake.pop(0)

    # Draw snake for the first time.
    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()

    # Refresh screen
    screen.update()

    # Rinse and repeat
    turtle.ontimer(move_snake, DELAY)


# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0)  # Turn off automatic animation.

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# Create snake as a list of coordinate pairs.
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

# Draw snake for the first time.
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

# Set animation in motion
move_snake()

# Finish nicely
turtle.done()
