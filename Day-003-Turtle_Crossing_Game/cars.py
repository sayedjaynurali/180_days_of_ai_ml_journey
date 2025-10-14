from turtle import Turtle
import random

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = 0.1
        self.penup()
        self.goto(320,random.randint(-280,280))
        self.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_len=2,stretch_wid=1)
        self.setheading(180)
    
    def move_left(self):
        self.forward(5)

    def increase_speed(self):
        self.car_speed *= 0.9
