from turtle import Turtle,Screen

initial_state = (0,-300)
class Tim(Turtle):
    def __init__(self):
        super().__init__()
        self.reset_game()
    
    def move_forward(self):
        new_y = self.ycor()+10
        self.goto(self.xcor(), new_y)

    def reset_game(self):
        self.penup()
        self.goto(initial_state)
        self.setheading(90)
        self.shape("turtle")
        self.color("black")