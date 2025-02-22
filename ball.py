from turtle import Turtle

class Ball(Turtle) :
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor,new_ycor)

    def bounceY(self):
        self.y_move *= -1
        
    def bounceX(self):
        self.x_move *= -1
        self.ball_speed *= 0.9
    
    def resetPosition(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounceX()
        self.bounceY()