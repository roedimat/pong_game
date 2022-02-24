from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.color("white")
        self.goto(-5, 275)
        self.display()


    def display(self):
        self.clear()
        self.write(f"{self.l_score} \t {self.r_score}", move=False,align=ALIGNMENT, font=FONT)


    def add_l_point(self):
        self.l_score += 1
        self.display()

    def add_r_point(self):
        self.r_score += 1
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME \t OVER", move=False,align=ALIGNMENT, font=FONT)