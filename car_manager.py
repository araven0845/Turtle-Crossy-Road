from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.pu()
            new_car.shapesize(1, 2)
            new_car.seth(180)
            new_car.goto(random.randint(340, 400), random.randint(-240, 240))
            self.cars.append(new_car)


    def drive(self):
        for car in self.cars:
            car.fd(self.speed)



    def speed_up(self):

        self.speed += MOVE_INCREMENT

