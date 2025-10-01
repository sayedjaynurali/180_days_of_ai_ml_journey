from turtle import Turtle,Screen,exitonclick
import time
import random
from paddle import Paddle
from ball import Ball
from scorebaord import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()  

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.center()  
        scoreboard.left_point()
    elif ball.xcor() < -380:
        ball.center()
        scoreboard.right_point()

screen.mainloop()