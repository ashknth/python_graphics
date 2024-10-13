from shapes import Line, Rectangle, Circle
import turtle

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
