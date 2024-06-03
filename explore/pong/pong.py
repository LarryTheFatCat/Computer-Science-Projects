"""
author: Tarkan Zarrouk
date: 06/03/2024
Pong game written in python and Pygame Zero
"""

# Imports
import os
import pgzrun

# Window Properties
WIDTH = 960
HEIGHT = 540
TITLE = "🏓 by Tarkan"
BG_COLOUR = (0,0,0) # Black
# Center pgz window
os.environ["SDL_VIDEO_CENTERED"] = "1"

# Game Objects
PADDLE_W = 30
PADDLE_H = 120
PADDLE_COLOUR = (255,255,255) # White
BALL_R = 15
BALL_COLOUR = (255,255,255) # White
# Left Paddle
LEFT_PADDLE = Rect(0,210, PADDLE_W, PADDLE_H)
# Right Paddle
RIGHT_PADDLE = Rect(WIDTH-PADDLE_W, 210, PADDLE_W, PADDLE_H)
# Ball
BALL = (WIDTH / 2, HEIGHT / 2)
# Scores
SCORE_LEFT = 10
SCORE_RIGHT = 8


def draw():
    # Set the background colour
    screen.fill(BG_COLOUR)
    
    # Draw the scores
    
    
    # Draw the paddles
    screen.draw.filled_rect(LEFT_PADDLE, PADDLE_COLOUR)
    screen.draw.filled_rect(RIGHT_PADDLE, PADDLE_COLOUR)
    
    # Draw the ball
    screen.draw.filled_circle(BALL, BALL_R, BALL_COLOUR)
    
def main():
    pgzrun.go()
    
main()