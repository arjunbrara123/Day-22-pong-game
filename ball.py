from turtle import Turtle                               # Import Turtle library for class inheritance


class Ball(Turtle):

    def __init__(self, pos=(0, 0)):
        """Initialise 'Ball' object as subclass of 'Turtle' object"""
        super().__init__()                              # Call 'turtle' initiation
        self.penup()                                    # Stop displaying trail
        self.shapesize(stretch_wid=1, stretch_len=1)    # Set dimensions of ball object to same height and width
        self.color("white")                             # Set colour to white
        self.shape("circle")                            # Set ball shape to round
        self.setpos(pos)                                # Move ball to desired position on screen
        self.x_dir = 1                                  # Set ball horizontal movement to right
        self.y_dir = 1                                  # Set ball vertical movement to up

    def move(self):
        """Move ball 10 spaces in currently set direction of travel"""
        if self.ycor() > 280: self.y_dir = -1           # Set vertical movement to down if ball at top of screen
        if self.ycor() < -280: self.y_dir = 1           # Set vertical movement to up if ball at bottom of screen
        new_x = self.xcor() + self.x_dir * 10           # Define 10 spaces forward in set horizontal dir of travel
        new_y = self.ycor() + self.y_dir * 10           # Define 10 spaces forward in set vertical dir of travel
        self.goto(new_x, new_y)                         # Move ball to newly defined position

    def bounce(self):
        """Bounce ball in opposite horizontal direction"""
        self.x_dir *= -1                                # Reverse horizontal direction of travel
