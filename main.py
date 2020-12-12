from turtle import Turtle, Screen   # Library for displaying GUI window
from scoreboard import Scoreboard   # Class object to display user scores
from paddle import Paddle           # Class object to create user paddles
from ball import Ball               # Class object for game ball that moves and bounces
import time                         # Library for pausing game between ball bounces to create animation effect

# Initialise the screen and environment
p1_score = 0                            # Initialise Player 1 score
p2_score = 0                            # Initialise Player 2 score
screen = Screen()                       # Initialise screen object
screen.setup(width=800, height=600)     # Set up screen dimensions
screen.bgcolor("black")                 # Set screen background colour to black
screen.title("Pong")                    # Set screen window title
screen.tracer(0)                        # Turn off automatic screen updates
scoreboard = Scoreboard()               # Initialise scoreboard object to show player scores
time_delay = 0.08                       # Set initial ball speed
winning_score = 3                       # Set points required to win game

# Create middle vertical line
donatello = Turtle()                # Initialise new turtle object
donatello.color("white")            # Set dash line colour to white
donatello.penup()                   # Ensure turtle isn't drawing on screen yet
donatello.setposition(0, -300)      # Set starting position of dashed line
donatello.setheading(90)            # Set direction to draw dashed line upwards
for i in range(60):                 # Set number of dashes to loop though
    donatello.penup()               # Lift pen off screen
    donatello.forward(10)           # Move forward without drawing line
    donatello.pendown()             # Put pen back on screen to start drawing again
    donatello.forward(10)           # Draw white line

# Initialise the paddles
p1 = Paddle((-350, 0))              # Player 1 Paddle starting position
p2 = Paddle((350, 0))               # Player 2 Paddle starting position
ball = Ball((0, 0))                 # Ball starting position
screen.update()                     # Update screen to let users see these

# Set up key listeners
screen.listen()
screen.onkey(p1.paddle_up, "q")         # Player 1 Paddle Up Key
screen.onkey(p1.paddle_down, "a")       # Player 1 Paddle Down Key
screen.onkey(p2.paddle_up, "Up")        # Player 2 Paddle Up Key
screen.onkey(p2.paddle_down, "Down")    # Player 2 Paddle Down Key


# Welcome 'Splash Screen' message
def splash_screen(scorer = 0):
    """Display Splash Screen 'PONG' message at start of each round"""
    splash = Turtle()               # Initialise Turtle object
    splash.hideturtle()             # Stop displaying turtle object on screen
    splash.penup()                  # Ensure turtle isn't drawing on screen yet
    if scorer > 0:                  # Check if a player recently scored
        splash.goto(0, 0)           # Goto centre of screen
        splash.color("gold")        # Set message text colour to gold
        splash.write(f"Player {scorer} scores!", align="center", font=("Courier", 40, "bold"))  # Set display font
        time.sleep(1)               # Keep on screen for 1 second
        screen.update()             # Update user
        splash.clear()              # Clear message
    splash.color("white")           # Set message text colour to white
    splash.setposition(0, -250)     # Set position of splash screen welcome message
    splash.speed(0)                 # Turn off any updating delays
    splash.write("PONG", align="center", font=("Courier", 80, "bold"))  # Set display font
    screen.update()                 # Update screen for user to see splash message
    time.sleep(1)                   # Keep on screen for 1 second
    splash.clear()                  # Clear splash screen message


# Initialise game loop
game_on = True                      # Set game looping variable for continuous loop
splash_screen()                     # Display splash screen welcome message
while game_on:                      # Start continuous game loop until someone wins!

    # Continuously move ball
    ball.move()                     # Move ball forward in set movement direction based on game rules

    # Check for collision with a paddle
    if ball.xcor() <= -320 and p1.distance(ball) < 50:
        ball.bounce()               # Bounce ball back towards Player 2
        time_delay *= 0.9           # Increase speed by 10%
        p1.color("yellow")          # Flash paddle 1 colour to yellow to indicate collision
        screen.update()             # Update screen for user
        ball.move()                 # Move ball back
        time.sleep(time_delay)      # Pause to let the user see
        p1.color("white")           # Reset paddle colour back to white

    if ball.xcor() >= 320 and p2.distance(ball) < 50:
        ball.bounce()               # Bounce ball back towards Player 1
        time_delay *= 0.9           # Increase speed by 10%
        p2.color("yellow")          # Flash paddle 2 colour to yellow to indicate collision
        screen.update()             # Update screen for user
        ball.move()                 # Move ball back
        time.sleep(time_delay)      # Pause to let the user see
        p2.color("white")           # Reset paddle colour back to white

    # Check if Player 2 has scored a point!
    if ball.xcor() <= -380:             # Check if ball crossed left of screen
        ball.setpos(0, 0)               # Reset ball position back to start
        p2_score += 1                   # Increase Player 2 score by 1
        scoreboard.refresh(p1_score, p2_score)  # Show updated score on screen
        time_delay = 0.08               # Reset ball speed
        if p2_score >= winning_score:   # Check if score increase is enough to win game
            scoreboard.winner(2)        # Show winner on scoreboard
            p1.color("red")             # Set Player 1 Paddle to Red to indicate loss
            p2.color("green")           # Set Player 2 Paddle to Green to indicate win
            game_on = False             # Stop game loop
        else:
            splash_screen(2)            # Splash screen to restart round

    # Check if Player 1 has scored a point!
    if ball.xcor() >= 380:              # Check if ball crossed left of screen
        ball.setpos(0, 0)               # Reset ball position back to start
        p1_score += 1                   # Increase Player 1 score by 1
        scoreboard.refresh(p1_score, p2_score)  # Show updated score on screen
        time_delay = 0.08               # Reset ball speed
        if p1_score >= winning_score:   # Check if score increase is enough to win game
            scoreboard.winner(1)        # Show winner on scoreboard
            p1.color("green")           # Set Player 1 Paddle to Green to indicate win
            p2.color("red")             # Set Player 2 Paddle to Red to indicate loss
            game_on = False             # Stop game loop
        else:
            splash_screen(1)            # Splash screen to restart round

    # Update screen
    time.sleep(time_delay)              # Pause game to facilitate visual animation
    screen.update()                     # Update screen

screen.exitonclick()                    # Keep game on screen until user clicks on the screen
