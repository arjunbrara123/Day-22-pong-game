from turtle import Turtle               # Import Turtle library for class inheritance

FONT_SCORE = ("Courier", 80, "bold")    # Font for displaying user scores at top
FONT_MSG = ("Courier", 40, "bold")      # Font for displaying messages in centre screen


class Scoreboard(Turtle):

    def __init__(self):
        """Initialise 'ScoreBoard' object as subclass of 'Turtle' object"""
        super().__init__()              # Call 'turtle' initiation
        self.hideturtle()               # Stop displaying turtle object on screen
        self.color("white")             # Set text colour to white
        self.penup()                    # Don't display trail
        self.refresh(0, 0)              # Display starting scores
        self.speed(0)                   # Turn off any updating delays

    def refresh(self, p1_score, p2_score, scorer=0, col="white"):
        """Show updated user scores on scoreboard"""
        self.clear()                                                # Clear existing scoreboard
        self.color(col)                                             # Set scoreboard text colour
        self.goto(-100, 180)                                        # Goto Top Left for Player 1 Score position
        if scorer == 1:                                             # Check if Player 1 scored
            self.color("gold")                                      # If scored, show Player 1 score in gold
        self.write(str(p1_score), align="center", font=FONT_SCORE)  # Display Player 1's current score
        self.color(col)                                             # Reset scoreboard text colour
        self.goto(100, 180)                                         # Goto Top Right for Player 2 Score position
        if scorer == 2:                                             # Check if Player 2 scored
            self.color("gold")                                      # If scored, show Player 2 score in gold
        self.write(str(p2_score), align="center", font=FONT_SCORE)  # Display Player 2's current score
        self.color(col)                                             # Reset scoreboard text colour

    def game_over(self):
        """Game over on screen"""
        self.goto(0, 0)                                                     # Goto centre of screen
        self.write("GAME OVER!", align="center", font=FONT_MSG)             # Write 'Game Over' message

    def winner(self, p_win):
        """Display winning player on screen"""
        self.goto(0, 0)                                                     # Goto centre of screen
        self.color("gold")                                                  # Change text colour to gold
        self.write(f"Player {p_win} wins!", align="center", font=FONT_MSG)  # Write winning player on screen

    def debug_mode(self):
        """Inform user of debugging mode is active"""
        self.goto(0, 0)                                                     # Goto centre of screen
        self.color("red")                                                   # Change text colour to red
        self.write("DEBUGGING MODE", True, align="center", font=FONT_MSG)   # Write 'Debugging Mode' on screen
