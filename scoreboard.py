from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        
        super().__init__()
        self.color('White')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
         
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=("Courier", 80, " normal"))    
        self.goto(-100,200)
        self.write(self.l_score, align='center', font=("Courier", 80, " normal"))
            
    #adding a point to right side
    def r_point(self):

        self.r_score += 1
        self.update_scoreboard()
    #adding a point to left side
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
       