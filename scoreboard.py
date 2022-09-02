from turtle import Turtle
ALIGNMENT = "center"
FONT_STYLE = ("Arial", 40, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 220)
        self.l_score = 0
        self.r_score = 0
        self.refresh()

    def increase_score_r(self):
        self.r_score += 1

    def increase_score_l(self):
        self.l_score += 1

    def refresh(self):
        self.clear()
        self.write(arg=f"{self.l_score} : {self.r_score}", move=False, align=ALIGNMENT, font=FONT_STYLE)

    def game_over(self, side):
        self.goto(0, 0)

        if side == "left":
            self.write("Left wins!", False, align=ALIGNMENT, font=FONT_STYLE)
        else:
            self.write("Right wins!", False, align=ALIGNMENT, font=FONT_STYLE)
