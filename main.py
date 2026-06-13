# Created by Agamdeep Singh
# Portfolio: https://linktr.ee/coderagam001


from turtle import Screen
from paddle import Paddle
from score import Scoreboard
from ball import Ball
from time import sleep


# Seting up the Screen
s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Pong Game")
s.tracer(0)

# Setting up the Paddle , Ball & Scoreboard
paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))
scoreboard = Scoreboard()
ball = Ball()

# Setting up the Controls
s.listen()
s.onkeypress(paddle_l.go_up, "w") 
s.onkeypress(paddle_l.go_down, "s") 
s.onkeypress(paddle_r.go_up, "Up")
s.onkeypress(paddle_r.go_down, "Down")

game_on = True
while game_on:
    sleep(ball.move_speed)
    s.update()
    ball.move()

    # Detect collisions with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collisions with the paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if the ball misses any of the paddles
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.point_l()
    
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.point_r()


s.exitonclick()