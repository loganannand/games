from turtle import Turtle
import random

FOOD_HEIGHT = 0.8
FOOD_WIDTH = 0.8
FOOD_SHAPE = 'square'
FOOD_COLOR = 'red'

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE) # Each food item is a circle
        self.penup() 
        self.shapesize(stretch_len=FOOD_HEIGHT, stretch_wid=FOOD_WIDTH) 
        self.color(FOOD_COLOR)
        self.speed('fastest')
        random_x, random_y = random.randint(-280, 280), random.randint(-280, 280) # generate random coordinates for food object
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x, random_y = random.randint(-280, 280), random.randint(-280, 280) # generate random coordinates for food object
        self.goto(random_x, random_y)

