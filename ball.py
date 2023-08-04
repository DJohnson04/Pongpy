from turtle import Turtle

import random
class Ball(Turtle):
    #constructor to set paddle values
    def __init__(self,l_paddle,r_paddle):
        super().__init__()
        self.l_paddle = l_paddle
        self.r_paddle = r_paddle
        self.goto(0,0)
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 1
        self.y_move = 1
    
    #methods to call to make the ball move at a random x and y point 
    def ball_move_randomly(self):
        new_x = self.xcor()+ self.x_move
        new_y = self.ycor()+ self.y_move
        self.goto(new_x, new_y)

    #methods to bounce the ball off of a object 
    #reverse the y 
    def bounce_y(self):
        self.y_move *= -1
    #revereses the x 
    def bounce_x(self):
        self.x_move *= -1
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
    
        