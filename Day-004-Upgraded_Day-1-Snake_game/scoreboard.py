from turtle import Turtle

alignment = "left"
text_font = ("Courier",25,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.display_score()

    def display_score(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(-80,270)
        self.write(f"Score: {self.score} High Score: {self.high_score}",move=False,align=alignment,font=text_font)
    
    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.display_score()

    def score_increase(self):
        self.clear()
        self.score += 1
        self.display_score()