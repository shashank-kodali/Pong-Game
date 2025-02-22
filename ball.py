from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()

    def move(self):
        new_xcor = self.xcor() + 10
        new_ycor = self.ycor() + 10
        self.goto(new_xcor,new_ycor)
