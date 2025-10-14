from turtle import Turtle

alignment = "left"
text_font = ("Courier",25,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(-10,270)

    def display_score(self):
        self.write(f"Score: {self.score}",move=False,align=alignment,font=text_font)
        # print(f"Score: {self.score}")
    
    def game_over(self):
        self.goto(-10,0)
        self.write("GAME OVER",move=False,align=alignment,font=text_font)
        

    def score_increase(self):
        self.clear()
        self.score += 1
        self.display_score()
        # print(f"Your Score is: {self.score}")