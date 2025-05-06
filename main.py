from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
my_screen=Screen()
my_screen.tracer(0)
food=Food()
scoreboard=Scoreboard()
my_screen.bgcolor("black")
my_screen.setup(width=600,height=600)
my_screen.title("Snake game")
snake=Snake()
my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.right,"Right")
my_screen.onkey(snake.left,"Left")
game_is_on=True
while game_is_on:
    my_screen.update()
    time.sleep(0.09)

    snake.move()
    #update score and snake length for every point taken
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.update()
        snake.extend()

    #define the boundaries for screen play
    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor() >280 or snake.head.ycor() <-280:
        scoreboard.game_over()
        game_is_on=False

    #game over if snake bites itself
    for segment in snake.segments:
        if segment== snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()

my_screen.exitonclick()