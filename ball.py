from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_dif = 3
        self.y_dif = 3

    def move(self):
        new_x = self.xcor() + self.x_dif
        new_y = self.ycor() + self.y_dif
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_dif *= -1

    def bounce_x(self):
        self.x_dif *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
