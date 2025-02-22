from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.updateScore()
        
    def updateScore(self):
        self.clear()
        self.goto(-80,230)
        self.write(self.l_score ,align= "center" ,font=("courier",50,"normal") )
        self.goto(80,230)
        self.write(self.r_score ,align= "center" ,font=("courier",50,"normal") )

    def lSocredPoint(self):
        self.l_score +=1
        self.updateScore()

    def rSocredPoint(self):
        self.r_score +=1
        self.updateScore()