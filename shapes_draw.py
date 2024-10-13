import turtle
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract class representing a generic geometric shape."""
    def __init__(self, color="black"):
        self.color = color  # Shape color
        self.t = turtle.Turtle()  # Turtle object to draw the shape
        self.t.hideturtle()
        self.t.speed(0)  # Fastest drawing speed

    @abstractmethod
    def draw(self):
        """Abstract method to draw the shape."""
        pass

class Line(Shape):
    """Class representing a line segment."""
    def __init__(self, x1, y1, x2, y2, color="black"):
        super().__init__(color)
        self.x1 = x1  # Starting x coordinate
        self.y1 = y1  # Starting y coordinate
        self.x2 = x2  # Ending x coordinate
        self.y2 = y2  # Ending y coordinate

    def draw(self):
        """Draws a line segment using the turtle object."""
        self.t.penup()
        self.t.goto(self.x1, self.y1)  # Move to the start position
        self.t.pendown()
        self.t.color(self.color)
        self.t.goto(self.x2, self.y2)  # Draw line to end position

class Rectangle(Shape):
    """Class representing a rectangle."""
    def __init__(self, x, y, width, height, color="black"):
        super().__init__(color)
        self.x = x  # Bottom-left x coordinate
        self.y = y  # Bottom-left y coordinate
        self.width = width
        self.height = height

    def draw(self):
        """Draws a rectangle using the turtle object."""
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()
        self.t.color(self.color)
        for _ in range(2):
            self.t.forward(self.width)
            self.t.left(90)
            self.t.forward(self.height)
            self.t.left(90)

class Circle(Shape):
    """Class representing a circle."""
    def __init__(self, x, y, radius, color="black"):
        super().__init__(color)
        self.x = x  # x coordinate of the center
        self.y = y  # y coordinate of the center
        self.radius = radius

    def draw(self):
        """Draws a circle using the turtle object."""
        self.t.penup()
        self.t.goto(self.x, self.y - self.radius)  # Adjust to draw circle from center
        self.t.pendown()
        self.t.color(self.color)
        self.t.circle(self.radius)

def draw_house():
    """Draws a house using shapes."""
    # Draw the house body
    house_body = Rectangle(-100, -100, 200, 200, color="blue")
    house_body.draw()

    # Draw the house roof (triangle made of lines)
    roof_left = Line(-100, 100, 0, 200, color="red")
    roof_left.draw()
    roof_right = Line(0, 200, 100, 100, color="red")
    roof_right.draw()
    roof_base = Line(-100, 100, 100, 100, color="red")
    roof_base.draw()

    # Draw the door
    door = Rectangle(-30, -100, 60, 100, color="brown")
    door.draw()

    # Draw windows (using small rectangles)
    window1 = Rectangle(-80, 0, 40, 40, color="white")
    window1.draw()
    window2 = Rectangle(40, 0, 40, 40, color="white")
    window2.draw()

def draw_stick_figure():
    """Draws a stick figure using shapes."""
    # Draw the head
    head = Circle(0, 50, 25, color="black")
    head.draw()

    # Draw the body
    body = Line(0, 25, 0, -50, color="black")
    body.draw()

    # Draw the arms
    left_arm = Line(0, 0, -50, -25, color="black")
    left_arm.draw()
    right_arm = Line(0, 0, 50, -25, color="black")
    right_arm.draw()

    # Draw the legs
    left_leg = Line(0, -50, -25, -100, color="black")
    left_leg.draw()
    right_leg = Line(0, -50, 25, -100, color="black")
    right_leg.draw()

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("House and Stick Figure Drawing")

    draw_house()
    draw_stick_figure()

    turtle.done()
