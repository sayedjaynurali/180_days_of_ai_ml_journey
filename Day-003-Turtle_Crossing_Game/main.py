from turtle import Turtle,Screen
from tim import Tim
from cars import Cars
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.tracer(0)
screen.bgcolor("white")
screen.title("The Turtle Crossing Game")
screen.setup(width=600,height=600)
screen.colormode(255)

tim = Tim()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(tim.move_forward,"Up")

cars = []
car_speed = 0.1

game_is_on = True
while game_is_on:
    time.sleep(car_speed)
    screen.update()

    if random.randint(1,6) == 1:
        new_car = Cars()
        cars.append(new_car)

    for car in cars:
        
        car.move_left()

        if tim.distance(car)<20:
            game_is_on = False
            scoreboard.game_over()

    if tim.ycor() > 280:
        tim.reset_game()
        scoreboard.update_level()
        car_speed *= 0.9
    
screen.mainloop()