from turtle import Screen, Turtle
import numpy as np 
import time
from snake import Snake
from food import Food
from score import ScoreBoard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('VIM Snake Game')
screen.tracer(0) # turn tracer off 

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'k')
screen.onkey(snake.down, 'j')
screen.onkey(snake.left, 'h')
screen.onkey(snake.right, 'l')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.05) # set refresh

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score() # increase score by 1 when collision occurs 

    # detect collision with walls
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset()

    # detect collision with snake tail 
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()

screen.exitonclick()
