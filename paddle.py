from turtle import Turtle                               # Import Turtle library for class inheritance


class Paddle(Turtle):

    def __init__(self, pos):
        """Initialise 'Paddle' object as subclass of 'Turtle' object"""
        super().__init__()                              # Call 'turtle' initiation
        self.penup()                                    # Stop displaying trail
        self.shapesize(stretch_wid=5, stretch_len=1)    # Stretch turtle to create a 'paddle' shape
        self.color("white")                             # Set colour to white
        self.shape("square")                            # Set paddle shape
        self.setpos(pos)                                # Move paddle to desired position on screen

    def paddle_up(self):
        """Move a paddle up"""
        self.sety(self.ycor() + 60)                     # Move paddle up 60 paces

    def paddle_down(self):
        """Move a paddle down"""
        self.sety(self.ycor() - 60)                     # Move paddle down 60 paces
