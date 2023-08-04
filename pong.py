from turtle import Screen, Turtle
from ball import Ball
from paddles import Paddle
import time
from scoreboard import Scoreboard

#create screen
screen = Screen()
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
screen.setup(1000,800)

#creating game objects
r_paddle = Paddle(400,0)
l_paddle = Paddle(-400,0)
ball = Ball(r_paddle,l_paddle)
scoreboard = Scoreboard() 

#moving paddle up and down
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "w")


#ball.ball_move_randomly()
game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.ball_move_randomly()

    #detect collision with wall
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    #detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 390 or ball.distance(l_paddle) < 50 and ball.xcor() < -390:
        ball.bounce_x()
    
    #detect right paddle misses
    if ball.xcor() > 480:
        ball.reset_position()
        scoreboard.l_point()
        
    
    #detect left paddle misses
    if ball.xcor() < -480:
        ball.reset_position()
        scoreboard.r_point()
        
screen.exitonclick()