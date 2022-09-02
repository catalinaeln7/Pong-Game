from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.go_up)
screen.onkeypress(key="Down", fun=r_paddle.go_down)

screen.onkeypress(key="w", fun=l_paddle.go_up)
screen.onkeypress(key="s", fun=l_paddle.go_down)

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 410:
        ball.reset_position()
        scoreboard.increase_score_l()
        scoreboard.refresh()

    # Detect L paddle misses
    if ball.xcor() < -410:
        ball.reset_position()
        scoreboard.increase_score_r()
        scoreboard.refresh()

    if scoreboard.l_score >= 10:
        game_is_on = False
        scoreboard.game_over("left")

    if scoreboard.r_score >= 10:
        game_is_on = False
        scoreboard.game_over("right")










screen.exitonclick()