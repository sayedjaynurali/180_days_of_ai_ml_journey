from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

scoreboard.display_score()
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.turtle_head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.score_increase()
    
    if snake.turtle_head.xcor() < -280 or snake.turtle_head.xcor() > 280 or snake.turtle_head.ycor() < -280 or snake.turtle_head.xcor() > 280:
        game_is_on = False
        scoreboard.game_over()
    
    for segment in snake.turtle_list:
        if segment == snake.turtle_head:
            pass
        elif snake.turtle_head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()