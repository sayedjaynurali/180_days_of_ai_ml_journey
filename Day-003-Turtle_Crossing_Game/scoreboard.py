from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("black")
        self.level = 0
        self.goto(-250,250)
        self.update_level()
    
    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}",align="left",font=("Courier",30,"normal"))
    
    def game_over(self):
        self.pencolor("black")
        self.goto(-20,0)
        self.write("GAME OVER",align="left",font=("Courier",30,"normal"))
