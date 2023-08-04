from turtle import Turtle
#self
class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.goto(x,y)
        self.shape('square')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color('white')
        self.penup()
   
   
    #creating self functions
    def go_up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)


