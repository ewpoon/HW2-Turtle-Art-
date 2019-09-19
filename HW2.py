# Your name: Erica Poon
# Your student id: 31778854
# Your email: ewpoon@umich.edu
# List who you worked with on this homework:

# import the turtle functions for use in this program
# don't need to use the module name
from turtle import *


def draw_rectangle(turtle, xpos, ypos, length, width, color):
    turtle.penup()
    turtle.color(color)
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.setheading(90)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()
   
    """
    Write a function to draw a rectangle on the screen
    with the specified parameters.

    :param turtle: An instance of the Turtle class
    :param xpos: The X-axis coordinate for a corner of the rectangle
    :param ypos: The Y-axis coordinate for a corner of the rectangle
    :param length: The length of the rectangle
    :param width: The width of the rectangle
    :param color: The line color and fill color to use for the rectangle
    """


def draw_background(turtle, coords, colors, length, width):
    output = list(zip(coords, colors))
    #turtle.penup()
    for (coord, color) in output:
        draw_rectangle(turtle, coord[0], coord[1], length, width, color)

    #for (x,y) in coords:
    #    for color in colors:
    #        draw_rectangle(turtle, x, y, length, width, color)

    """
    Write a function to draw four rectangles by calling draw_rectangle().
    This function should call draw_rectangle() in a loop.

    :param turtle: An instance of the Turtle class
    :param coords: A list of (X,Y) coordinates to cycle through
    :param colors: A list of colors to cycle through
    :param length: The length of the rectangles
    :param width: The width of the rectangles
    """

def draw_spiral(turtle, xpos, ypos, color, width):
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.color(color)
    turtle.pensize(width)
    turtle.pendown()
    turtle.speed(10)

    for i in range(150):
        turtle.forward(i)
        turtle.right(50)

    
    """
    Write a function to draw a spiral on top of your 4 rectangles.
    The function should contain the following parameters at a minimum,
    but feel free to add additional ones like "size" or "direction",
    if you'll be calling this function more than once.

    :param turtle: An instance of the Turtle class
    :param xpos: The X-axis coordinate where the spiral should begin.
    :param ypos: The Y-axis coordinate where the spiral should begin.
    :param color: The color of the line.
    :param width: The width of the line.
    """

def draw_star(turtle, xpos, ypos, length, color):
    turtle.color(color)
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.setheading(120)
    turtle.pensize(2)
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(length)
        turtle.left(144)
    turtle.end_fill()

def draw_E(turtle, xpos, ypos, x, y, z, color):
    turtle.color(color)
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(90)
    points = [x, y, z]
    for i in points:
        turtle.penup()
        turtle.goto(xpos, i)
        turtle.pendown()
        turtle.forward(25)

def draw_P(turtle, xpos, ypos, color):
    turtle.color(color)
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(90)

    for i in range(3):
        turtle.forward(25)
        turtle.right(90)
    
def draw_initials(turtle):
    draw_E(turtle, -25, -300, -250, -275, -300, 'white')
    draw_P(turtle, 10, -300, 'white')

def draw_art(turtle, coords, colors, color, length, width, penwidth, xpos, ypos):
    draw_background(turtle, coords, colors, length, width)
    draw_spiral(turtle, xpos, ypos, color, penwidth)
    draw_initials(turtle)
    draw_star(turtle, -250, 240, 20, 'white')
    draw_star(turtle, -189, 158, 10, 'white')
    draw_star(turtle, -5, 239, 30, 'white')
    draw_star(turtle, -258, 38, 10, 'white')
    draw_star(turtle, -186, 288, 15, 'white')

    """
    Write a function to create your abstract art by calling draw_background and
    draw_spiral (at least once). Feel free to modify the arguments of this
    function as you like. But you should pass in the turtle object at the very
    least.

    Extra credit for using additional functions to draw shapes other than
    a square/rectangle, triangle, or spiral. And for signing your art
    with your initials in block letters.
    """


def main():
    alex = Turtle()
    space = Screen()
    coords = [(0, 0), (300, 0), (300, -300), (0, -300)]
    colors = ['midnight blue', 'blue', 'dodger blue', 'deep sky blue']

    draw_art(alex, coords, colors, 'light sky blue', 300, 300, 2, 0, 0)
    space.exitonclick()

    """
    Write a main function that will be called when you run this program
    from the terminal.

    Make sure to create a Screen object, a Turtle object,
    and call draw_background and draw_spiral (at least once).
    You'll also want to create your lists of coordinates and colors here.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting untill you close the drawing window.
    """

    pass


# Only run the main method if this file is executed (not imported)
if __name__ == '__main__':
    main()
