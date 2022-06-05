# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @coderagam001 / @codewithagam
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh


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
scoreboard1 = Scoreboard((-20, 260))
scoreboard2 = Scoreboard((20, 260))
ball = Ball()

# Setting up the Controls
s.listen()
s.onkey(paddle_l.go_up, "w") 
s.onkey(paddle_l.go_down, "s") 
s.onkey(paddle_r.go_up, "Up")
s.onkey(paddle_r.go_down, "Down")

game_on = True
while game_on:
    sleep(0.1)
    s.update()
    ball.move()

    # Detect collisions with the wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # Detect collisions with the paddle
    if (ball.distance(paddle_l) < 50 and ball.xcor() > 320) or (ball.distance(paddle_r) < 50 and ball.xcor() > -320):
        ball.bounce_x()

    # Detect if the ball misses any of the paddles
    if ball.xcor() > 380:
        ball.reset()
        scoreboard1.score += 1
        scoreboard1.update()
    
    if ball.xcor() < -380:
        ball.reset()
        scoreboard2.score += 1
        scoreboard2.update()

s.exitonclick()